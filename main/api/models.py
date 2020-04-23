from django.db import models
from django.contrib.auth.models import User
from api.managers import CommentManager, RequestReceiveManager, RequestSendManager, NotificationManager


class Clinic(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    rating = models.IntegerField(default=None)

    class Meta:
        verbose_name = 'Clinic'
        verbose_name_plural = 'Clinics'


class Comment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinic_comments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    content = models.TextField(max_length=1000, default='')
    comments = CommentManager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return "{0}: {1}".format(self.created_by, self.clinic)


class DoctorInfo(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    age = models.IntegerField(default=None)
    working_experience = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Doctor(DoctorInfo):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Request(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_requests')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinic_request')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_request')
    created_at = models.DateTimeField()
    description = models.CharField(max_length=200)

    requests = RequestSendManager()
    requests = RequestReceiveManager()
    objects = requests

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'


class Notification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notifications')
    msg = models.TextField(max_length=100)
    notifications = NotificationManager()

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return "Dear {} you have new message".format(self.to_user.username)
