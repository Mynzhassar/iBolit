from django.urls import path

from core.views.view_sets import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('clinics', ClinicViewSet)
router.register('departments', DepartmentDetailedViewSet)
router.register('services', OrderToServiceViewSet)
router.register('doctors', OrderToDoctorViewSet)

urlpatterns =router.urls