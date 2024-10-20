from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import User
from django.urls import reverse

def register_view(request) :
    if request.method == 'POST' :
        post_data = request.POST
        email = post_data.get('email')
        password = post_data.get('password')

        test_user = authenticate(request, email=email, password=password)

        if test_user :
            return JsonResponse({'error': 'email has alredy been used'}, status=200)
        else :
            user = User.objects.create_user(email=email, password=password)
            user.save()
            return JsonResponse({'success': f'{reverse('login')}'}, status=200)

    else :
        return render(request, 'auth/register.html')