from django.contrib import admin
from profiles.models import *

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = [
    'user',
    'resume',
    'profile_image',
    'profile_summary',
    'education',
    'year_of_passout',
    'previous_employment',
    'projects',
    'certification',
    'skills',
    'socials',
    'address',
    'date_of_birth',
    'language',
    'marital_status',
    'created_on',
    'updated_on'
]


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = [
    'user',
    'hiring_for',
    'pan_number',
    'official_email',
    'company_address',
    'created_at',
    'updated_at'
]

