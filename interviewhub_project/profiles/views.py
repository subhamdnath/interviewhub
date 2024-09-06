from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.models import *

def candidate_view(request):
    if request.method == "POST":

        resume = request.POST.get("resume")
        profile_image = request.POST.get("profile_image")
        profile_summary = request.POST.get("profile_summary")
        education = request.POST.get("education")
        year_of_passout = request.POST.get("year_of_passout")
        previous_employment = request.POST.get("previous_employment")
        projects = request.POST.get("projects")
        socials = request.POST.get("socials")
        address = request.POST.get("address")
        date_of_birth = request.POST.get("date_of_birth")
        language = request.POST.get("language")
        marital_status = request.POST.get("marital_status")


        if not resume:
            messages.error(request, "Please enter resume.", extra_tags='resume')
            return redirect ('register')
        if not profile_image:
            messages.error(request, "Please enter profile_image.", extra_tags='profile_image')
            return redirect ('register')   
        if not profile_summary:
            messages.error(request, "Please enter profile_summary.", extra_tags='profile_summary')
            return redirect ('register')  
        if not education:
            messages.error(request, "Please enter education.", extra_tags='education')
            return redirect ('register') 
        if not year_of_passout:
            messages.error(request, "Please enter year_of_passout.", extra_tags='year_of_passout')
            return redirect ('register')
        if not previous_employment:
            messages.error(request, "Please enter previous_employment.", extra_tags='previous_employment')
            return redirect ('register')
        if not projects:
            messages.error(request, "Please enter projects.", extra_tags='projects')
            return redirect ('register')   
        if not socials:
            messages.error(request, "Please enter socials.", extra_tags='socials')
            return redirect ('register')  
        if not address:
            messages.error(request, "Please enter address.", extra_tags='address')
            return redirect ('register') 
        if not date_of_birth:
            messages.error(request, "Please enter date_of_birth.", extra_tags='date_of_birth')
            return redirect ('register')
        if not language:
            messages.error(request, "Please enter language.", extra_tags='language')
            return redirect ('register') 
        if not marital_status:
            messages.error(request, "Please enter marital_status.", extra_tags='marital_status')
            return redirect ('register')
        

        candidate = Candidate.objects.create(user = request.user,
                                            resume = resume, 
                                            profile_image = profile_image,
                                            profile_summary = profile_summary, 
                                            education = education, year_of_passout = year_of_passout,
                                            previous_employment = previous_employment,
                                            projects = projects, socials = socials,
                                            address = address, date_of_birth = date_of_birth,
                                            language = language, marital_status = marital_status)
        messages.success(request, "Candidate profile updated successfully", extra_tags= "candidate")
        return redirect("register")


def employer_view(request):
    if request.method == "POST":

        hiring_for = request.POST.get("hiring_for")
        pan_number = request.POST.get("pan_number")
        official_email = request.POST.get("official_email")
        company_address = request.POST.get("company_address")

        if not hiring_for:
            messages.error(request, "Please enter hiring_for.", extra_tags='hiring_for')
            return redirect ('register')   
        if not pan_number:
            messages.error(request, "Please enter pan_number.", extra_tags='pan_number')
            return redirect ('register')  
        if not official_email:
            messages.error(request, "Please enter official_email.", extra_tags='official_email')
            return redirect ('register') 
        if not company_address:
            messages.error(request, "Please enter company_address.", extra_tags='company_address')
            return redirect ('register')

        employer = Employer.objects.create(user = request.user, hiring_for = hiring_for,
                                           pan_number = pan_number, 
                                           official_email = official_email,
                                           company_address = company_address)
        
        messages.success(request, "Employer profile created successfully", extra_tags= "employer")
        return redirect("register")



