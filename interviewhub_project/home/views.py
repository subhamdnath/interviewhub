from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from home.models import MyUser



def home_view(request):
    return render(request, "home/home.html")


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        try:
            full_name = request.POST.get("full_name")
            email = request.POST.get("email")
            phone_number = request.POST.get("phone_number")
            age = request.POST.get("age")
            state = request.POST.get("state")
            gender = request.POST.get("gender")
            role = request.POST.get("role")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")

            if len(password) < 6:
                messages.error(request, "Password must have at least 6 characters.", extra_tags='password_character')
                return redirect('register')
            
            if password != confirm_password:
                messages.error(request, "Password and confirm password do not match.", extra_tags='password_confirm_password')
                return redirect('register')

            if MyUser.objects.filter(email=email).exists():
                messages.error(request, "An account already exists with this email.", extra_tags='email_exists')
                return redirect('register')
            

            user = MyUser.objects.create(full_name = full_name, email = email,
                                        phone_number = phone_number, age = age,
                                        state = state, gender = gender, role = role,
                                        password = password)
            user.set_password(password)
            user.save()

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

        if not email or not password:
            messages.error(request, "Email or password is missing",
                           extra_tags="missing")
            return redirect ("login")

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect("job")
        else:
            messages.error(request, "User not found. Please register- ",
                            extra_tags="failed_login")
            return redirect ("login")
     
    return render(request, "home/login.html")


def job_view(request):
    return render(request, "home/job.html")























































        # if not full_name:
        #     messages.error(request, "Please enter full_name.", extra_tags='full_name')
        #     return redirect ('register')
        # if not email:
        #     messages.error(request, "Please enter email.", extra_tags='email')
        #     return redirect ('register')   
        # if not phone_number:
        #     messages.error(request, "Please enter phone_number.", extra_tags='phone_number')
        #     return redirect ('register')  
        # if not age:
        #     messages.error(request, "Please enter age.", extra_tags='age')
        #     return redirect ('register') 
        # if not state:
        #     messages.error(request, "Please enter state.", extra_tags='state')
        #     return redirect ('register')
        # if not gender:
        #     messages.error(request, "Please enter gender.", extra_tags='gender')
        #     return redirect ('register')
        # if not role:
        #     messages.error(request, "Please enter role.", extra_tags='role')
        #     return redirect ('register')

        # if not password:
        #     messages.error(request, "Please enter password.", extra_tags='password')
        #     return redirect ('register')
        # if not confirm_password:
        #     messages.error(request, "Please enter confirm_password.", extra_tags='confirm_password')
        #     return redirect ('register')