from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import MyUser



def home_view(request):
    return render(request, "home/home_view.html")

def register_view(request):
    if request.method == "POST":

        full_name = request.POST.get("Full Name")
        email = request.POST.get("Email")
        username = request.POST.get("Username")
        phone_number = request.POST.get("Phone Number")
        password = request.POST.get("Password")
        confirm_password = request.POST.get("Confirm Password")

        if password != confirm_password:
            messages.error(request, "Password and Confirm Password doesn't match.")
        
        if MyUser.objects.filter(email = email).exists():
            messages.error(request, "Email already exists")

        if full_name and email and username and phone_number and password:
            user = MyUser.objects.create(full_name = full_name, email = email,
                                         username = username, phone_number = phone_number,
                                         password = password)
            user.set_password(password)
            messages.success(request,"User registered successfully")
            return redirect("login")

    return render(request, "home/register_view.html")


























def login_view(request):
    return render(request, "home/login_view.html")

def job_view(request):
    return render(request, "home/job.html")

