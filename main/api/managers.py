from django.db import models


class CommentManager(models.Model):
    def created_by_user(self, user):
        return super().filter(created_by=user)

    def created_by_user_detailed(self, user, pk):
        return super().filter(created_by=user, pk=pk)


class RequestSendManager(models.Model):
    def patients_requests(self, user):
        return super().filter(patient=user)


class RequestReceiveManager(models.Model):
    def doctors_requests(self, clinic, doctor):
        return super().filter(clinic=clinic, doctor=doctor)


class NotificationManager(models.Model):
    def get_notifications(self, user):
        return super().filter(toUser=user)

