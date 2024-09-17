from django.db import models
from home.constrains import *
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("The Email field must set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)
    




class User(AbstractUser):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
    mobile_code = models.CharField(max_length=30, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, default= "Prefer not to say", choices=GENDER_CHOICES) 
    profile_pic = models.FileField(upload_to='profile_pic/', blank=True, unique=True)
    state = models.CharField(max_length=50, choices=INDIAN_STATES_AND_UTS,)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Admin", null=True, blank=True)
    social_id = models.CharField(max_length=255, null=True, blank=True)
    social_type = models.CharField(max_length=20, choices=SOCIAL_TYPE, null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        managed = True
        db_table = "tbl_user"
     
    def __str__(self):
        return f"{self.email}-{self.role}"
    
    
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











            
