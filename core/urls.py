from django.urls import path
from core.views.views import ClinicCreateListDelete


urlpatterns = [
    path("clinics/", ClinicCreateListDelete.as_view())
]