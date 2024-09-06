from django.db import models
from home.models import *
from profiles.models import *
from home.constrains import *


class Job(models.Model):

    '''Multiple jobs can be posted by a single employer'''
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    '''Company name, location can be filtered out from employer table '''
    job_title = models.CharField(max_length=255, db_index=True)
    job_summary = models.CharField(max_length=500, null=True, blank=True)
    job_location = models.CharField(max_length=255, db_index=True, null=True, blank=True)
    job_category = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPE_TYPES, null=True, blank=True)
    job_description = models.TextField()
    
    no_of_openings = models.PositiveBigIntegerField(null=True, blank=True)
    required_skills = models.CharField(max_length=255, null=True, blank=True)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    years_of_experience = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True) 
    employment_type = models.CharField(max_length=20, choices= EMPLOYMENT_TYPES, null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)

    candidates_applied = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "tbl_job"
    
    def __str__(self):
        return f"{self.employer.user.email} - {self.job_title}"





