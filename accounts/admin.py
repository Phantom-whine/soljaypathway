from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin) :
    list_display = ['email', 'phone', 'country', 'job_of_interest']
    search_fields = ['country', 'job_of_interest']
    readonly_fields = ['phone']
    list_filter = ['country', 'job_of_interest']

admin.site.site_header = 'SolJayPathway'
admin.site.site_title = 'SolJay'