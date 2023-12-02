from django.db import models
from django.contrib.postgres.fields import ArrayField


class ClinicRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_number = models.BigIntegerField(unique=True)
    working_days = ArrayField(models.CharField(max_length=200))
    responsible_person = models.ForeignKey('Doctor', on_delete=models.PROTECT)
    internal_phone_number = models.CharField(max_length=40)

    class Meta:
        db_table = 'ClinicRoom'

class Doctor(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    date_of_empoloyment = models.DateField()
    education = models.CharField(max_length=40)
    date_of_resignation = models.DateField()
    contract_details = models.CharField(max_length=40)

    class Meta:
        db_table = 'Doctor'

class Patient(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'Patient'


class Visit(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=200)
    recommendation = ArrayField(models.CharField(max_length=200))
    date_of_visit = models.DateField()
    payment = models.IntegerField(default=0)
    class Meta:
        db_table = 'Visit'
class MedicalCard(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    visit_date = models.DateField()
    diagnosis = ArrayField(models.CharField(max_length=200))
    current_condition = models.CharField(max_length=100)
    recommendations = ArrayField(models.CharField(max_length=200))
    visits = models.ManyToManyField(Visit, related_name='MedicalCards')
    class Meta:
        db_table = 'MedicalCard'
