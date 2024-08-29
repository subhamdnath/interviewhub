from django.db import models
from home.constrains import *
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    username = models.CharField(max_length=255, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null = True, blank=True)
    email = models.EmailField(verbose_name="email_address", max_length=255, unique=True, null=True, blank=True)

    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=50, choices=INDIAN_STATES_AND_UTS,)
    gender = models.CharField(max_length=20, default= "Prefer not to say", choices=GENDER_CHOICES) 
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Admin", null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "tbl_user"
     
    def __str__(self):
        return f"{self.email}-{self.role}"
            










            
