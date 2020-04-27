from django.db import models
from utils.constants import *
from utils import validators
from core.managers import ClinicManager, DepartmentManager, OrderManager, ServiceManager
from users.models import MyUser
from utils.validators import *
from utils.upload import *


class Clinic(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default="Dostyk 55")
    info = models.TextField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=1)
    status = models.PositiveSmallIntegerField(choices=CLINIC_STATUSES, default=CLINIC_STATE)
    # creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='clinics')

    objects = ClinicManager()

    # def is_owner(self, request):
    #     return self.creator.id == request.user.id

    # def __str__(self):
    #     return self.title


class Department(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    direction = models.PositiveSmallIntegerField(choices=CLINIC_DEPARTMENTS, default=THERAPEUTIC_DEPARTMENT)
    info = models.TextField(max_length=100)
    floor = models.PositiveSmallIntegerField()

    objects = DepartmentManager()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.info


class Service(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    title = models.PositiveSmallIntegerField(choices=CLINIC_SERVICES)
    price = models.FloatField()
    cabinet = models.CharField(max_length=5)

    objects = ServiceManager()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.cabinet


class Staff(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media',
                               validators=[validators.validate_document_size,
                                           validators.validate_document_extension],
                               null=True, blank=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Doctor(Staff):
    experience = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)


class Consultant(Staff):
    phone = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Consultant"
        verbose_name_plural = "Consultants"

    def __str__(self):
        return f"{self.surname} {self.name}"


class Order(models.Model):
    client = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='my_orders_to_doctor', null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='my_orders_to_service', null=True)
    created_at = models.DateTimeField(auto_now=True)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_TYPES, default=PAYMENT_VIA_CASH)
    date = models.CharField(max_length=10000)
    time = models.CharField(max_length=255)

    objects = OrderManager()

    def __str__(self):
        return self.date


class TherapyDocument(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    therapy = models.FileField(upload_to=therapy_document_path,
                               validators=[therapy_document_size, therapy_document_extension],
                               null=True, blank=True)
