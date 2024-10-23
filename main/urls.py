from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create-job-listing/', views.job_create, name='job-create'),
    path('job-listing/<uuid:id>/', views.job_detail, name='job-detail'),
    path('apply/<uuid:id>', views.apply, name='apply'),
    path('applied-jobs/', views.applied_jobs, name='applied'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('applied-jobs/<uuid:id>/details/', views.job_applied_detail, name='details-a'),
    path('discard-request/<uuid:id>', views.discard_application, name='delete-app'),
    path('aquire-permit/', views.permit, name='permit'),
    path('', views.home, name='home'),
]