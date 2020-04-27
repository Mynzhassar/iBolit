from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from core.models import Clinic, Department



@receiver(post_save, sender=Clinic)
def department_create(sender, instance, **kwargs):
    Department.objects.create(clinic=instance, name='THERAPEUTIC_DEPARTMENT', direction=1)
    Department.objects.create(clinic=instance, name='SURGERY_DEPARTMENT', direction=2)
    Department.objects.create(clinic=instance, name='TRAUMA_DEPARTMENT', direction=3)
    Department.objects.create(clinic=instance, name='NEUROSURGICAL_DEPARTMENT', direction=4)
    Department.objects.create(clinic=instance, name='CARDIAC_DEPARTMENT', direction=5)
    Department.objects.create(clinic=instance, name='INTENSIVE_CARE_DEPARTMENT', direction=6)