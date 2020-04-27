from django.urls import path

from core.views.view_sets import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('clinics', ClinicViewSet)
router.register('departments', DepartmentDetailedViewSet)
router.register('services', OrderToServiceViewSet)
router.register('doctors', OrderToDoctorViewSet)
<<<<<<< HEAD
router.register('orders',OrderViewSet)
urlpatterns =router.urls
=======

urlpatterns = router.urls
>>>>>>> c81c7530f19485d13ddeeb64a2fea7c19a2282b3
