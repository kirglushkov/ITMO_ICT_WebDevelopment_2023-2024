from rest_framework import generics, status
from base.models import ClinicRoom, MedicalCard, Patient, Visit, Doctor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum
from .serializers import ClinicRoomSerializer, DoctorSerializer, PatientSerializer
import urllib.parse
from django.db.models import Q

import logging

# Create a logger instance with the name of the current module
logger = logging.getLogger(__name__)
@api_view(['GET'])
def getCostByDateNDoctor(req):
    #  Вычислить суммарную стоимость лечения пациентов по дням и по врачам.
    # by given doctor or day, count payment in visit model

    # /cost-by-date/?date=1962-10-27
    # /cost-by-date/?doctor_id=1

    doctor_id = req.query_params.get('doctor_id', None)
    date = req.query_params.get('date', None)
    queryset = Visit.objects.all()

    if doctor_id is not None:
        queryset = queryset.filter(id=doctor_id)
    if date is not None:
        queryset = queryset.filter(date_of_visit=date)

    cost_by_date = queryset.values('date_of_visit').annotate(total_cost=Sum('payment'))
    return Response(cost_by_date, status=status.HTTP_200_OK)


@api_view(['GET'])
def getPatientsByDate(req):
    # Количество приемов пациентов по датам.

    # /patients-by-date/?date=1962-10-27
    date = req.query_params.get('date', None)
    if date is not None:
        patients_count_by_date = Visit.objects.filter(date_of_visit=date).count()
    else:
        patients_count_by_date = Visit.objects.all().values('date_of_visit').annotate(count=Count('patient'))
    
    return Response(patients_count_by_date, status=status.HTTP_200_OK)

@api_view(['GET'])
def getListPatientsPaid(req):
    # Список пациентов, уже оплативших лечение.
    # iterate thru medicalCard and find patients who made payment, retrieve ids, and then return 
    # from Patient all info 
    paid_patients = Visit.objects.exclude(payment__exact='0').values_list('patient', flat=True)
    patients = Patient.objects.filter(id__in=paid_patients)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getDoctors(req):
    #retrieve all doctors
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getPatientsbyDoctorName(req):
    #retrieve all patients of given doctor name, then go to model class MedicalCard(models.Model):\

    # http://127.0.0.1:8000/doctor-patients/?name=%D0%9C%D0%B0%D0%BA%D1%81%D0%B8%D0%BC
    doctor_name = req.query_params.get('name', None)
    decoded_str = urllib.parse.unquote(doctor_name)
    if decoded_str:
        doctor = Doctor.objects.filter(Q(first_name__icontains=decoded_str) | Q(last_name__icontains=decoded_str)).first()
        if doctor:
            medical_records = Visit.objects.filter(doctor=doctor).values('date_of_visit', 'payment')
            return Response(medical_records, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getNumbersOfPatientsOtoronginolog(req):
    #retrieve all patients phone_numbers of given doctor specialization = "Отоларинголог" and patient date_of_birth > 1987
    # steps to do:
    # search for doctor specialization = "Отоларинголог", save id's
    # find from id's medical cards, then there will be column patient with id, and save those id's and find them in model
    # patient, retrieve all patients date_of_birth > 1987
    otolaryngologists = Doctor.objects.filter(specialization="Отоларинголог").values_list('id', flat=True)
    medical_cards = MedicalCard.objects.filter(doctor_id__in=otolaryngologists)
    patient_ids = medical_cards.values_list('patient', flat=True)
    patients = Patient.objects.filter(id__in=patient_ids, date_of_birth__year__gt=1987).values('phone_number')
    return Response(patients, status=status.HTTP_200_OK)


@api_view(['GET'])
def getDoctorByDay(req):
    # Вывести список врачей, в графике которых среди рабочих дней имеется
    # заданный.
    # /doctor-by-day/?day=Пятница
    day = req.query_params.get('day', None)
    decoded_str = urllib.parse.unquote(day)
    if decoded_str:
        clinic_rooms = ClinicRoom.objects.filter(working_days__contains=[decoded_str])
        # doctors = [room.responsible_person for room in clinic_rooms]
        serializer = ClinicRoomSerializer(clinic_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getPatients(req):
    #retrieve all patients
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getVisitReport(req):
    # Отчет о работе врачей в заданный промежуток времени с указанием списка
    #принятых пациентов, их диагноза и стоимости услуг с вычислением
    #суммарного дохода по каждому врачу.

    # /visit-report/?start_date=1956-01-01&end_date=2023-02-01 
    start_date = req.query_params.get('start_date')
    end_date = req.query_params.get('end_date')

    if start_date and end_date:
        visit = Visit.objects.filter(date_of_visit__range=[start_date, end_date])
        report_data = visit.values('doctor').annotate(
            total_income=Sum('payment'),
            patients=Count('patient'),
        ).order_by('doctor')
        
        for record in report_data:
            doctor_id = record['doctor']
            doctor_info = Doctor.objects.get(pk=doctor_id)
            record['doctor'] = DoctorSerializer(doctor_info).data
        return Response(report_data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


