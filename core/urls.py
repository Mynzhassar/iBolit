from django.urls import path
from core.views.views import ClinicAPIView, ClinicDetailedApiView

from core.views.view_sets import DepartmentViewSet, DoctorViewSet, ConsultantViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'departments', DepartmentViewSet, basename="core")
router.register(r'doctors', DoctorViewSet, basename="core")
router.register(r'consultants', ConsultantViewSet, basename="core")

urlpatterns = [
    path("clinics/", ClinicAPIView.as_view()),
    path("clinics/<int:pk>/", ClinicDetailedApiView.as_view())
              ] + router.urls
