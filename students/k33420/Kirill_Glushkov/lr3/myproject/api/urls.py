from django.urls import path
from .views import (
    getCostByDate,
    getPatientsByDate,
    getListPatientsPaid,
    getDoctors,
    getDoctorPatients,
    getNumbersOfPatientsOtoronginolog,
    getDoctorByDay,
    getPatients,
    getVisitReport,
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cost-by-date/', getCostByDate, name='cost-by-date'),
    path('patients-by-date/', getPatientsByDate, name='patients-by-date'),
    path('list-patients-paid/', getListPatientsPaid, name='list-patients-paid'),
    path('doctors/', getDoctors, name='doctors'),
    path('doctor-patients/', getDoctorPatients, name='doctor-patients'),
    path('numbers-of-patients-otorhinolaryngologist/', getNumbersOfPatientsOtoronginolog, name='numbers-of-patients-otorhinolaryngologist'),
    path('doctor-by-day/', getDoctorByDay, name='doctor-by-day'),
    path('patients/', getPatients, name='patients'),
    path('visit-report/', getVisitReport, name='visit-report'),
]

urlpatterns = format_suffix_patterns(urlpatterns)