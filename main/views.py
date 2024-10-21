from django.shortcuts import render
from .models import Job

def home_view(request) :
    content = dict()
    if request.user.is_authenticated :
        user_countries = request.user.country_of_choice.split(',')
        query = request.GET.get('q', None)
        jobs = Job.objects.filter(country__in = user_countries).order_by('-created')
        if query :
            jobs = jobs.filter(title__icontains = query)
            content['q'] = query
            
        content['jobs'] = jobs
        
    return render(request, 'main/dashboard.html', content)