from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه')
    avatar = models.ImageField(upload_to='images/profile/', null=True, blank=True, verbose_name='آواتار')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name == "" and self.last_name == "":
            return self.username
        return f'{self.first_name} {self.last_name}'
