from django.db import models
from home.constrains import *
from home.models import User

class Candidate(models.Model): 
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume", null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)
    profile_summary = models.CharField(max_length=255, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    year_of_passout = models.DateField(null=True, blank=True)
    previous_employment = models.CharField(max_length=255, null=True, blank=True)
    projects = models.CharField(max_length=255, null=True)
    certification = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    socials = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    marital_status = models.CharField(max_length=30, default="Prefer not to say", choices=MARITAL_STATUS_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.user.email}"
    class Meta:
        db_table = "tbl_candidate"


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hiring_for = models.CharField(max_length=30, default="Company",choices=HIRING_FOR_CHOICE)
    pan_number = models.CharField(max_length=10, null=True, blank=True)
    official_email = models.EmailField(null=True, blank=True)
    company_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.user.email}"
    class Meta:
        db_table = "tbl_employer"

    

