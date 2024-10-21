from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager

class User(AbstractUser) :
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    country_of_choice = models.CharField(max_length=250)
    job_of_interest = models.CharField(max_length=250)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    class Meta :
        ordering = ['country']

    def __str__(self):
        return self.email