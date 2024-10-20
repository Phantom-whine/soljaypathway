from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager

class User(AbstractUser) :
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()
    def __str__(self):
        return self.email