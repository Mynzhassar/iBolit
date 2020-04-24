from django.db import models
from core.constants import *
from django.db.models import Q
from datetime import datetime
from users.models import MyUser

class ClinicManager(models.Manager):


    def state_clinics(self):
        return self.filter(status=CLINIC_STATE)

    def private_clinics(self):
        return self.filter(status=CLINIC_PRIVATE)

    def filter_by_status(self,status):
        return self.filter(status=status)

class Clinic(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    info = models.TextField()
    status = models.PositiveSmallIntegerField(choices=CLINIC_STATUSES, default=CLINIC_STATE)

    objects = ClinicManager()

    def __str__(self):
        return self.title

class DepartmentManager(models.Manager):
    def filter_by_department(self,direction):
        return self.filter(direction=direction)

class Department(models.Model):
    direction = models.PositiveSmallIntegerField(choices=CLINIC_DEPARTMENTS, default=THERAPEUTIC_DEPARTMENT)
    info = models.TextField()
    floor = models.PositiveSmallIntegerField()
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE, related_name='departments')

    objects = DepartmentManager()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.direction


class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


    class Meta:
        abstract = True

class Doctor(Person):
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    cabinet = models.PositiveSmallIntegerField()
    salary = models.IntegerField()
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='doctors')
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name='doctors')

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return '{} {}'.format(self.surname, self.name)


class Service(models.Model):
    title = models.PositiveSmallIntegerField(choices=CLINIC_SERVICES)
    price = models.FloatField()
    cabinet = models.IntegerField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title


class OrderManager(models.Manager):
##    def get_active(self):
##        return self.filter(due_to__gte=datetime.now())
##
##  def get_expired(self):
##      return self.filter(due_to__lte=datetime.now())
##
    def get_done_cash(self):
        return self.filter(Q(due_to__lte=datetime.now()) & Q(payment_type=PAYMENT_VIA_CASH))

    def get_done_card(self):
        return self.filter(Q(due_to__lte=datetime.now()) & Q(payment_type=PAYMENT_VIA_CARD))


class Order(models.Model):
    client = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='my_orders')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='my_doctors', null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='my_services', null=True)
    created_at = models.DateTimeField(auto_now=True)
    payment_type = models.PositiveSmallIntegerField(choices=PAYMENT_TYPES, default=PAYMENT_VIA_CASH)
    date = models.CharField(max_length=10000)

    objects = OrderManager()

    def __str__(self):
        pass













