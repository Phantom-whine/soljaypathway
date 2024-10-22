from django.contrib import admin
from .models import Job, Applied

@admin.register(Job)
class JobAdmin(admin.ModelAdmin) :
    list_display = ['title', 'job_type', 'country', 'salary']
    list_filter = ['job_type', 'country', 'gender_required']
    search_fields = ['title', 'description']

@admin.register(Applied)
class A_admin(admin.ModelAdmin) :
    list_display = ['first_name', 'last_name' ,'payed']
