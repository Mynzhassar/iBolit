import datetime
from django.db import models
from django.db.models import Q

from utils.constants import *


class ClinicManager(models.Manager):

    def state_clinics(self):
        return self.filter(status=CLINIC_STATE)

    def private_clinics(self):
        return self.filter(status=CLINIC_PRIVATE)

    def filter_by_status(self, status):
        return self.filter(status=status)


class DepartmentManager(models.Manager):
    def filter_by_department(self, direction):
        return self.filter(direction=direction)


class OrderManager(models.Manager):
    # def get_active(self):
    #     return self.filter(due_to__gte=datetime.now())

    # def get_expired(self):
    #     return self.filter(due_to__lte=datetime.now())

    def get_done_cash(self):
        return self.filter(Q(due_to__lte=datetime.now()) & Q(payment_type=PAYMENT_VIA_CASH))

    def get_done_card(self):
        return self.filter(Q(due_to__lte=datetime.now()) & Q(payment_type=PAYMENT_VIA_CARD))
