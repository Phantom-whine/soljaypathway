from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .models import User
from django.urls import reverse

def register_view(request) :
    if request.method == 'POST' :
        post_data = request.POST
        email = post_data.get('email')
        password = post_data.get('password')
        job_of_interest = post_data.get('job_interest')
        country = post_data.get('country')
        country_of_choice = post_data.get('country-of-choice')
        phone = post_data.get('phone')

        test_user = authenticate(request, email=email, password=password)

        if test_user :
            return HttpResponse('Email has been used by you')
        else :
            user = User.objects.create_user(email=email, password=password)
            user.phone = phone
            user.country = country
            user.country_of_choice = country_of_choice
            user.country = country
            user.save()
            messages.error(request, 'Email has alredy been used')
            return redirect(reverse('login'))

    else :
        return render(request, 'auth/register.html')

def login_view(request) :
    if request.method == 'POST' :
        post_data = request.POST
        email = post_data.get('email')
        password = post_data.get('password')

        user = authenticate(request, email=email, password=password)
        if user :
            if user.is_active == True :
                login(request, user)
                return HttpResponse(f'Logged in as {email}')
            else :
                return HttpResponse(f'Account for {email} has been banned')

        else :
            return HttpResponse(f'Account for {email} does not exists')

    else :
        return render(request, 'auth/login.html')