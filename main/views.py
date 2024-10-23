from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Applied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .decorators import check_payment

@login_required(redirect_field_name='login')
def dashboard_view(request) :
    content = dict()
    if request.user.is_authenticated :
        user_countries = request.user.country_of_choice.split(',')
        query = request.GET.get('q', None)
        jobs = None
        if request.user.is_staff != True :
            jobs = Job.objects.filter(country__in = user_countries).order_by('-created')
        else :
            jobs = Job.objects.all().order_by('-created')

        if query :
            jobs = jobs.filter(title__icontains = query)
            content['q'] = query

        try:
            pag_obj = Paginator(jobs, 12)
            page_number = request.GET.get('page', 1)
            jobs = pag_obj.get_page(page_number)
        except EmptyPage :
            jobs = pag_obj.get_page(pag_obj.num_pages)
        except PageNotAnInteger :
            jobs = pag_obj.get_page(1)
            
        content['jobs'] = jobs
        
    return render(request, 'main/dashboard.html', content)

@login_required(redirect_field_name='login')
def job_create(request) :
    if request.method == 'POST' :
        files = request.FILES
        post_data = request.POST
        image = files.get('image')
        title = post_data.get('title')
        country = post_data.get('country')
        city = post_data.get('city')
        children_info = post_data.get('children_info')
        job_start = post_data.get('job_start')
        time_of_stay = post_data.get('time_of_stay')
        working_hours = post_data.get('working_hours')
        gender_required = post_data.get('gender_required')
        has_pet = post_data.get('has_pet')
        parent_age_group = post_data.get('parent_age_group')
        letter_to_applicant = post_data.get('letter_to_applicant')
        description = post_data.get('description')
        salary = post_data.get('salary')
        job_type = post_data.get('job_type')

        new_job = Job.objects.create(
            image=image,
            title=title,
            country=country,
            city=city,
            children_info=children_info,
            job_start=job_start,
            time_of_stay=time_of_stay,
            working_hours=working_hours,
            gender_required=gender_required,
            has_pet=has_pet,
            age_group=parent_age_group,
            letter_to_applicant=letter_to_applicant,
            description=description,
            salary = salary,
            job_type=job_type
        )

        new_job.save()
        messages.info(request, 'Job listing created.')
        return redirect(reverse('dashboard'))
    else :
        return render(request, 'main/create_job.html')

@login_required(redirect_field_name='login')
@check_payment
def job_detail(request, id) :
    job = get_object_or_404(Job, id=id)
    return render(request, 'main/job-details.html', {'job':job, 'id': id})

@login_required(redirect_field_name='login')
@check_payment
def apply(request, id) :
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST' :
        files = request.FILES
        post_data = request.POST
        first_name = post_data.get('first-name')
        last_name = post_data.get('last-name')
        location = post_data.get('location')
        cv = files.get('cv')
        info = post_data.get('other-info')
        
        new_application = Applied.objects.create(
            first_name=first_name,
            last_name=last_name,
            current_location=location,
            cv_image=cv,
            info=info,
            user=request.user,
            job=job
        )

        new_application.save()
        # return redirect('https://soljay.lemonsqueezy.com/buy/256aa511-235a-42c0-8d58-ebe5ab6f1668')
        messages.success(request, 'Job application submitted!')
        return redirect(reverse('applied'))
    else :
        if Applied.objects.filter(user=request.user, job=job) :
            return render(request, 'main/already.html')
        
        return render(request, 'main/apply-job.html', {'job': job, 'id': id})

@login_required(redirect_field_name='login')
def applied_jobs(request) :
    content = dict()
    if request.user.is_authenticated :
        query = request.GET.get('q', None)
        jobs = None
        if request.user.is_staff == True :
            jobs = Applied.objects.all()
        else :
            jobs = Applied.objects.filter(user=request.user)

        if query :
            jobs = jobs.filter(job__title__icontains = query)
            content['q'] = query

        try:
            pag_obj = Paginator(jobs, 12)
            page_number = request.GET.get('page', 1)
            jobs = pag_obj.get_page(page_number)
        except EmptyPage :
            jobs = pag_obj.get_page(pag_obj.num_pages)
        except PageNotAnInteger :
            jobs = pag_obj.get_page(1)
            
        content['jobs'] = jobs
        
    return render(request, 'main/applied-jobs.html', content)

def about(request) :
    return render(request, 'main/about.html')

def contact(request) :
    return render(request, 'main/contact.html')

@login_required(redirect_field_name='login')
def job_applied_detail(request, id) :
    job_application = get_object_or_404(Applied, id=id)
    return render(request, 'main/applied-details.html', {'job':job_application, 'id': id})

@login_required(redirect_field_name='login')
def discard_application(request, id) :
    obj = get_object_or_404(Applied, id=id)
    if obj.user.email == request.user.email :
        obj.delete()
        messages.info(request, 'Job application deleted successfully!')
        return redirect(reverse('applied'))
    else :
        return render(request, 'main/404.html')
    
@login_required(redirect_field_name='login')
def permit(request) :
    return render(request, 'main/work_permit.html')

def home(request) :
    return render(request, 'main/home.html')