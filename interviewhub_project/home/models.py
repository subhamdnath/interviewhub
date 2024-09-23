from django.db import models
from home.constrains import *
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

#https://www.geeksforgeeks.org/creating-custom-decorator-in-django-for-different-permissions/
    

class UserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault("is_admin", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True")
        
        return self.create_user(email, password, **extra_fields)
    
    def create_candidate(self, email, password, **extra_fields):
        extra_fields.setdefault("is_candidate",True)

        if extra_fields.get("is_candidate") is not True:
            raise ValueError("Candidate must have is_candidate=True")
        
        return self.create_user(email, password, **extra_fields)
    
    def create_employee(self, email, password, **extra_fields):
        extra_fields.setdefault("is_employee", True)
        if extra_fields.get("is_employee") is not True:
            raise ValueError("Employee must have is_employee True")
        
        return self.create_user(email, password, **extra_fields)
    


class User(AbstractUser):

    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null = True)  
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_code = models.CharField(max_length=30, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    gender = models.CharField(max_length=20, default= "Prefer not to say", choices=GENDER_CHOICES, null=True) 
    profile_pic = models.FileField(upload_to='profile_pic/', blank=True)
    state = models.CharField(max_length=50, choices=INDIAN_STATES_AND_UTS, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Candidate")
    social_id = models.CharField(max_length=255)
    social_type = models.CharField(max_length=20, choices=SOCIAL_TYPE, null=True)
    password = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    is_candidate = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    


    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        managed = True
        db_table = "tbl_user"
     
    def __str__(self):
        return f"{self.email}-{self.role}-{self.id}"
    
    
class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=255, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "tbl_review"

    def __str__(self):
        return f"{self.user.email} - {self.user.email}"
    

class Language(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=100, )











            
