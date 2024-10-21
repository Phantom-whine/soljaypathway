from django.db import models
from accounts.models import User
from django.utils import timezone

TYPE = (
    ('normal', 'Normal'),
    ('offer', 'Offer')
)

class Job(models.Model) :
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=3000)
    price_for_application = models.PositiveIntegerField(default=0)
    amount_of_applicants = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    job_type = models.CharField(
        max_length=20,
        choices=TYPE,
        default='normal'
    )

    class Meta :
        ordering = ['-title']

    def __str__(self) :
        return self.title

STATUS = (
    ('pending', 'pending'),
    ('approved', 'approved')
)

class A_Job(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices = STATUS,
        default = 'pending'
    )

    def __str__(self) :
        return self.job