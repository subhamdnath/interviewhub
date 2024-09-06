from django.shortcuts import render, redirect
from django.contrib import messages 
from candidate.models import *


def apply_job_view(request):
    if request.method == "POST":

        job = request.POST.get("job")

        if not job:
            messages.error(request, "Please enter job.", extra_tags='job')
            return redirect ('register')
        
        applyjob = ApplyJob.objects.create(candidate = request.user,
                                           job = job)
        
        messages.success(request, "Job applied successfully", extra_tags= "applyjob")
        return redirect("register")
