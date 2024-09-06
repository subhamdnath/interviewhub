from home.models import *
from django.db import models
from profiles.models import *
from employer.models import *


class ApplyJob(models.Model):

    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    '''Employer name can be filtered out from Job model'''
    job = models.ManyToManyField(Job )
    '''A job can be applied by multiple candidates and a candidate can apply multiple jobs'''
    
    applied_date = models.DateField(auto_now=True, null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        managed = True
        db_table = "tbl_applyjob"
    
    def __str__(self):
        return f"{self.candidate.user.email} - {self.job}"