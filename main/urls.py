from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.home_view, name='dashboard'),
]