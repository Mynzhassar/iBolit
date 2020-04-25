from django.db import models
from utils.constants import *
from core.managers import ClinicManager, DepartmentManager, OrderManager
from users.models import MyUser


class Clinic(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    info = models.TextField()
    rating = models.PositiveSmallIntegerField(default=1)
    status = models.PositiveSmallIntegerField(choices=CLINIC_STATUSES, default=CLINIC_STATE)

    objects = ClinicManager()

    def __str__(self):
        return self.title


class Department(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    direction = models.PositiveSmallIntegerField(choices=CLINIC_DEPARTMENTS, default=THERAPEUTIC_DEPARTMENT)
    info = models.TextField()
    floor = models.PositiveSmallIntegerField()

    objects = DepartmentManager()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.direction


class Staff(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='photos/', null=True, blank=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    job_title = models.IntegerField()
    salary = models.IntegerField()
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Doctor(Staff):
    experience = models.PositiveSmallIntegerField()
    cabinet = models.IntegerField()

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return '{} {}'.format(self.surname, self.job_title)


class Consultant(Staff):
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Consultant"
        verbose_name_plural = "Consultants"

    def __str__(self):
        return f"{self.surname} {self.name}"


class Service(models.Model):
    title = models.PositiveSmallIntegerField(choices=CLINIC_SERVICES)
    price = models.FloatField()
    cabinet = models.IntegerField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class Order(models.Model):
    client = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='my_orders')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='my_doctors', null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='my_services', null=True)
    consultant = models.ForeignKey(Consultant,on_delete=models.CASCADE,related_name='my_calls',null=True)
    created_at = models.DateTimeField(auto_now=True)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_TYPES, default=PAYMENT_VIA_CASH)
    date = models.CharField(max_length=10000)
    time = models.CharField(max_length=255)

    objects = OrderManager()

    def __str__(self):
        return self.date
