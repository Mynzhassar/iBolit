from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser



class MainUser(AbstractUser):
    is_creator = models.BooleanField(default=False)
    is_executor = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'

class Profile(models.Model):
    user = models.ForeignKey(MainUser,on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    address = models.CharField(max_length=300)
    avatar = models.FileField()


    def __str__(self):
        return self.user.username