from rest_framework import serializers
from base.models import ClinicRoom, Doctor, Patient
from django.db.models import Sum

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ClinicRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicRoom
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'specialization']
