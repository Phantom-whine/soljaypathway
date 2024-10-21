from django.contrib import admin
from .models import Job, A_Job

@admin.register(Job) 
class JobAdmin(admin.ModelAdmin) :
    list_display = ['title', 'price_for_application', 'job_type']
    list_filter = ['job_type', 'price_for_application']
    search_fields = ['title', 'description']
    readonly_fields = ['amount_of_applicants']

@admin.register(A_Job)
class A_Job_Admin(admin.ModelAdmin) :
    list_display = ['user', 'job', 'status']
    list_filter = ['status']
    search_fields = ['job']
