from rest_framework import generics, status
from base.models import ClinicRoom, MedicalCard, Patient, Visit, Doctor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Sum
from .serializers import DoctorSerializer, PatientSerializer


@api_view(['GET'])
def getCostByDate(req):
    #  Вычислить суммарную стоимость лечения пациентов по дням и по врачам.
    # by given doctor or day, count payment in visit model

    doctor_id = req.query_params.get('doctor_id', None)
    date = req.query_params.get('date', None)
    queryset = MedicalCard.objects.all()

    if doctor_id is not None:
        queryset = queryset.filter(id=doctor_id)
    if date is not None:
        queryset = queryset.filter(visit_date=date)

    cost_by_date = queryset.values('visit_date').annotate(total_cost=Sum('payment'))
    return Response(cost_by_date, status=status.HTTP_200_OK)


@api_view(['GET'])
def getPatientsByDate(req):
    # Количество приемов пациентов по датам.
    date = req.query_params.get('date', None)
    if date is not None:
        patients_count_by_date = MedicalCard.objects.filter(visit_date=date).count()
    else:
        patients_count_by_date = MedicalCard.objects.all().values('visit_date').annotate(count=Count('patient'))
    
    return Response(patients_count_by_date, status=status.HTTP_200_OK)

@api_view(['GET'])
def getListPatientsPaid(req):
    # Список пациентов, уже оплативших лечение.
    # iterate thru medicalCard and find patients who made payment, retrieve ids, and then return 
    # from Patient all info 
    paid_patients = MedicalCard.objects.exclude(payment__exact='0').values_list('patient', flat=True)
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
def getDoctorPatients(req):
    #retrieve all patients of given doctor name, then go to model class MedicalCard(models.Model):
    doctor_name = req.query_params.get('name', None)
    if doctor_name:
        doctor = Doctor.objects.filter(Q(first_name__icontains=doctor_name) | Q(last_name__icontains=doctor_name)).first()
        if doctor:
            medical_records = MedicalCard.objects.filter(doctor=doctor).values('visit_date', 'payment')
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
    day = req.query_params.get('day', None)
    if day:
        clinic_rooms = ClinicRoom.objects.filter(working_days__contains=[day])
        doctors = [room.responsible_person for room in clinic_rooms]
        serializer = DoctorSerializer(doctors, many=True)
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
    start_date = req.query_params.get('start_date')
    end_date = req.query_params.get('end_date')

    if start_date and end_date:
        medical_cards = MedicalCard.objects.filter(visit_date__range=[start_date, end_date])
        report_data = medical_cards.values('doctor').annotate(
            total_income=Sum('payment'),
            patients=Count('patient'),
        ).order_by('doctor')
        
        for record in report_data:
            doctor_id = record['doctor']
            doctor_info = Doctor.objects.get(pk=doctor_id)
            record['doctor'] = DoctorSerializer(doctor_info).data
        return Response(report_data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


