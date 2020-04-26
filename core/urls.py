from django.urls import path
from core.views.views import ClinicAPIView, ClinicDetailedApiView

from core.views.view_sets import ClinicViewSet
from rest_framework import routers

router = routers.DefaultRouter()

# router.register(r'clinics', ClinicViewSet, basename="core")
# router.register(r'departments', DepartmentViewSet, basename="core")
# router.register(r'orders', OrderViewSet, basename="core")

urlpatterns = [
    path("clinics/", ClinicAPIView.as_view()),
    path("clinics/<int:pk>/", ClinicDetailedApiView.as_view())
              ] + router.urls
