from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from accounts.models import User
from django.urls import reverse
import uuid

class Job(models.Model) :
    PETS = (
        ('yes', 'yes'),
        ('no', 'no')
    )
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    job_type = models.CharField(max_length=250)
    children_info = models.CharField(max_length=250)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    job_start= models.CharField(max_length=40)
    time_of_stay = models.CharField(max_length=40)
    letter_to_applicant = models.TextField()
    has_pet = models.CharField(choices=PETS, max_length=3)
    age_group = models.CharField(max_length=50, default=None)
    working_hours = models.CharField(max_length=50)
    salary = models.PositiveIntegerField(default=0)
    gender_required = models.CharField(max_length=10, choices=GENDER)
    created = models.DateTimeField(default=timezone.now)
    thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(400, 400)],  # Resize to 100x100 pixels
                                format='PNG',
                                options={'quality': 90})

    class Meta :
        ordering = ['-created']

    def __str__(self) :
        return self.title

    def get_absolute_url(self) :
        return reverse('job-detail', args=[self.id])

class Applied(models.Model) :
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    payed = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=100, default=None)
    last_name = models.CharField(max_length=100, default=None)
    current_location = models.CharField(max_length=100, default=None)
    info = models.TextField(default=None)
    cv_image = models.ImageField(upload_to='cv-images/', default=None)

    class Meta :
        ordering = ['-date']

    def __str__(self) :
        return self.job.title
    
    def get_absolute_url(self) :
        return reverse('details-a', args=[self.id])