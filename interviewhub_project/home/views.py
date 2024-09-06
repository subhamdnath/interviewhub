from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import re
from home.models import User
from django.contrib.auth.hashers import make_password


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            mobile_no = request.POST.get("mobile_no")
            state = request.POST.get("state")
            gender = request.POST.get("gender")
            role = request.POST.get("role")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            if not username:
                messages.error(request, "Please enter username.", extra_tags='username')
                return redirect ('register')
            if not first_name:
                messages.error(request, "Please enter first_name.", extra_tags='first_name')
                return redirect ('register')   
            if not last_name:
                messages.error(request, "Please enter last_name.", extra_tags='last_name')
                return redirect ('register')  
            if not email:
                messages.error(request, "Please enter email.", extra_tags='email')
                return redirect ('register') 
            if not mobile_no:
                messages.error(request, "Please enter mobile_no.", extra_tags='mobile_no')
                return redirect ('register')
            if not state:
                messages.error(request, "Please enter state.", extra_tags='state')
                return redirect ('register')
            if not gender:
                messages.error(request, "Please enter gender.", extra_tags='gender')
                return redirect ('register')
            if not role:
                messages.error(request, "Please enter role.", extra_tags='role')
                return redirect ('register')
            if not password:
                messages.error(request, "Please enter password.", extra_tags='password')
                return redirect ('register')
            if not confirm_password:
                messages.error(request, "Please enter confirm_password.", extra_tags='confirm_password')
                return redirect ('register')
            
            if len(password) < 6:
                messages.error(request, "Password must have at least 6 characters.", extra_tags='password_character')
                return redirect('register')
            
            if password != confirm_password:
                messages.error(request, "Password and confirm password do not match.", extra_tags='password_confirm_password')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "An account already exists with this email.", extra_tags='email_exists')
                return redirect('register')
         
            email_pattern = r'[a-zA-Z0-9._%+-]+@gmail\.com$'
            if not re.match(email_pattern, email):
                messages.error(request, "Please enter a valid Gmail address (example@gmail.com).", extra_tags='invalid_email')
                return redirect('register')
            

            user = User.objects.create(username = username, first_name = first_name,
                                       last_name = last_name, email = email,
                                        mobile_no = mobile_no,  state = state,
                                        gender = gender, role = role,
                                        password = make_password(password))
        

            messages.success(request, "User registered successfully! Please login to continue.", extra_tags="register")
            return redirect("login")

        except Exception as e:
            print(f"Error occurred: {e}")
            messages.error(request, "Something went wrong during registration. Please try again.", extra_tags='register_error')
            return redirect('register')
    
    return render(request, "home/register.html")



@csrf_exempt
def login_view(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email:
                messages.error(request, "Please enter email.", extra_tags='email')
                return redirect ('login')
        if not password:
                messages.error(request, "Please enter password.", extra_tags='password')
                return redirect ('login')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect("job")
        else:
            messages.error(request, "User not found. Please register- ",
                            extra_tags="failed_login")
            return redirect ("login")
     
    return render(request, "home/login.html")



def home_view(request):
    return render(request, "home/home.html")



def job_view(request):
    return render(request, "home/job.html")























































