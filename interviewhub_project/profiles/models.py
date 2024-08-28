from django.db import models
from home.models import MyUser

class CandidateProfile(models.Model):

    candidate = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume", blank=True)
    profile_image = models.ImageField(upload_to="profile_image",blank=True)
    profile_summary = models.CharField(max_length=255, null =True)
    education = models.CharField(max_length=255, null=True)
    year_of_passout = models.DateField(null = True)
    previous_employment = models.CharField(max_length=255, null=True)
    projects = models.CharField(max_length=255, null=True)
    certification = models.CharField(max_length=255, null=True)
    skills = models.CharField(max_length=255, null=True)

    address = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null= True)
    language = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null = True)
    marital_status = models.CharField(max_length=30, default="Prefer not to say", 
                                      choices=(("Single", "Single"),
                                                ("Married", "Married"),
                                                ("Prefer not to say", "Prefer not to say")))

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.candidate}-{self.candidate.email}"
    class Meta:
        db_table = "CandidateProfile"
    

class EmployerProfie(models.Model):
    employer = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    hiring_for = models.CharField(max_length=30, default="Company",choices=(("Company", "Company"),
                                                                             ("individual", "individual")))
    pan_number = models.CharField(max_length=10, null=True)
    official_email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.employer}-{self.employer.email}"
    class Meta:
        db_table = "EmployerProfie"

    

