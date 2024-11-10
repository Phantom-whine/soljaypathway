from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomManager
import uuid

class User(AbstractUser) :
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=250)
    country = models.CharField(max_length=250, null=True)
    country_of_choice = models.CharField(max_length=250, null=True)
    job_of_interest = models.CharField(max_length=250, null=True)
    permit = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()

    class Meta :
        ordering = ['country']

    def __str__(self):
        return self.email
    
    def save_user(self, *args, **kwargs) :
        if self.is_staff :
            self.country = 'None'
            self.permit = True
            self.job_of_interest = 'None'
            self.country_of_choice = 'None'
            
            self.save(*args, **kwargs)
            
        else :
            self.save(*args, **kwargs)