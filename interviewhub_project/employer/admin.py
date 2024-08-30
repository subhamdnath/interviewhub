from django.contrib import admin
from employer.models import *

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
    'employer',
    'job_title',
    'job_summary',
    'job_location',
    'job_category',
    'job_type',
    'job_description',
    'no_of_openings',
    'required_skills',
    'expected_salary',
    'years_of_experience',
    'department',
    'candidates_applied',
    'employment_type',
    'education',
    'created_by',
    'created_at',
    'updated_at'
]

