from django.urls import path, re_path
from .views import (
    getCostByDateNDoctor,
    getPatientsByDate,
    getListPatientsPaid,
    getDoctors,
    getPatientsbyDoctorName,
    getNumbersOfPatientsOtoronginolog,
    getDoctorByDay,
    getPatients,
    getVisitReport,
)
from rest_framework.urlpatterns import format_suffix_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Schema view for Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Healthcare API",
      default_version='v1',
      description="API endpoints for the Healthcare project",
      terms_of_service="#",
      contact=openapi.Contact(email="contact@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('cost-by-date/', getCostByDateNDoctor, name='cost-by-date'),
    path('patients-by-date/', getPatientsByDate, name='patients-by-date'),
    path('list-patients-paid/', getListPatientsPaid, name='list-patients-paid'),
    path('doctors/', getDoctors, name='doctors'),
    path('doctor-patients/', getPatientsbyDoctorName, name='doctor-patients'),
    path('numbers-of-patients-otorhinolaryngologist/', getNumbersOfPatientsOtoronginolog, name='numbers-of-patients-otorhinolaryngologist'),
    path('doctor-by-day/', getDoctorByDay, name='doctor-by-day'),
    path('patients/', getPatients, name='patients'),
    path('visit-report/', getVisitReport, name='visit-report'),
    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),

]

# Format suffix patterns
urlpatterns = format_suffix_patterns(urlpatterns)