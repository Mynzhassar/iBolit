from django.urls import path
from core.views.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clinics', ClinicViewSet)


urlpatterns = router.urls