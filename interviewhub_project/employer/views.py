from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.models import Employer
from employer.models import Job


def JobView(request):
    if request.method == "POST":

        job_title = request.POST.get("job_title")
        job_summary = request.POST.get("job_summary")
        job_location = request.POST.get("job_location")
        job_category = request.POST.get("job_category")
        job_type = request.POST.get("job_type")
        job_description = request.POST.get("job_description")

        no_of_openings = request.POST.get("no_of_openings")
        required_skills = request.POST.get("required_skills")
        expected_salary = request.POST.get("expected_salary")
        years_of_experience = request.POST.get("years_of_experience")
        department = request.POST.get("department")
        employment_type = request.POST.get("employment_type")
        education = request.POST.get("education")

        candidates_applied = request.POST.get("candidates_applied")
        created_by = request.POST.get("created_by")

        if not job_title:
            messages.error(request, "Please enter job_title.", extra_tags='job_title')
            return redirect ('register')
        if not job_summary:
            messages.error(request, "Please enter job_summary.", extra_tags='job_summary')
            return redirect ('register')   
        if not job_location:
            messages.error(request, "Please enter job_location.", extra_tags='job_location')
            return redirect ('register')  
        if not job_category:
            messages.error(request, "Please enter job_category.", extra_tags='job_category')
            return redirect ('register') 
        if not job_type:
            messages.error(request, "Please enter job_type.", extra_tags='job_type')
            return redirect ('register')
        if not job_description:
            messages.error(request, "Please enter job_description.", extra_tags='job_description')
            return redirect ('register')
        
        if not no_of_openings:
            messages.error(request, "Please enter no_of_openings.", extra_tags='no_of_openings')
            return redirect ('register')   
        if not required_skills:
            messages.error(request, "Please enter required_skills.", extra_tags='required_skills')
            return redirect ('register')  
        if not expected_salary:
            messages.error(request, "Please enter expected_salary.", extra_tags='expected_salary')
            return redirect ('register') 
        if not years_of_experience:
            messages.error(request, "Please enter years_of_experience.", extra_tags='years_of_experience')
            return redirect ('register')
        if not department:
            messages.error(request, "Please enter department.", extra_tags='department')
            return redirect ('register') 
        if not employment_type:
            messages.error(request, "Please enter employment_type.", extra_tags='employment_type')
            return redirect ('register')
        if not education:
            messages.error(request, "Please enter education.", extra_tags='education')
            return redirect ('register')
        
        employer = Employer.objects.get()

        job = Job.objects.create(job_title = job_title, 
                                job_summary = job_summary, job_location = job_location,
                                job_category = job_category, job_type = job_type, 
                                job_description = job_description,
                                no_of_openings = no_of_openings, required_skills = required_skills,
                                expected_salary = expected_salary, years_of_experience = years_of_experience,
                                department = department,
                                employment_type = employment_type, education = education, 

                                employer = request.user, 
                                created_by = request.user,
                                candidates_applied = candidates_applied ) 
        job.save()
        messages.success(request, "Job created successfully", extra_tags= "Job_create_success")
        return redirect( "home")
    return render(request, "home/register.html" )

        


