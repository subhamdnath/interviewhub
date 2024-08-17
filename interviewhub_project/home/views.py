from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, "home/home_view.html")

def job_view(request):
    return render(request, "home/job.html")

