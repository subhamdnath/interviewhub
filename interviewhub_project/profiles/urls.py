from django.urls import re_path
from profiles.views import *
from profiles.api_view import *

urlpatterns = [

    re_path(r'^employer_profile/$', EmployerProfileAPI.as_view(), name="employer-profile-api"),


]