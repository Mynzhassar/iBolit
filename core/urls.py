from django.urls import path

from core.views.view_sets import *
from core.views.cbv import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('clinics', ClinicViewSet)
router.register('departments', DepartmentDetailedViewSet)
router.register('services', OrderToServiceViewSet)
router.register('doctors', OrderToDoctorViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('clinic/', ClinicAPIView.as_view()),
    path("clinic/<int:pk>/", ClinicDetailedApiView.as_view())
              ] + router.urls
