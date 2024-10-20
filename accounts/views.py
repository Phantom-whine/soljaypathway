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

        test_user = authenticate(request, email=email, password=password)

        if test_user :
            return HttpResponse('Email has been used by you')
        else :
            user = User.objects.create_user(email=email, password=password)
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