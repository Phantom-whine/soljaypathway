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

        test_user = User.objects.filter(email=email).exists()

        if test_user :
            messages.error(request, f'Email {email} has already been used!')
            return redirect(reverse('register'))
        else :
            user = User.objects.create_user(email=email, password=password)
            user.phone = phone
            user.country = country
            user.country_of_choice = country_of_choice
            user.country = country
            user.job_of_interest = job_of_interest
            user.save()
            messages.success(request, f'Account for {email} created succesfully')
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
                messages.success(request, f'Logged in as {email}.')
                login(request, user)
                return redirect(reverse('dashboard'))
            else :
                messages.error(request, f'Account for {email} has been banned')
                return redirect(reverse('login'))

        else :
            messages.error(request, f'Incorrect Email or Password')
            return redirect(reverse('login'))

    else :
        return render(request, 'auth/login.html')

def logout_view(request) :
    logout(request)
    messages.info(request, 'Logged out!')
    return redirect(reverse('home'))