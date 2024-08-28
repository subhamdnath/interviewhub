from django.urls import path
from home.views import *

urlpatterns = [
    path('', home_view, name="home" ),
    path('register/', register_view, name="register" ),
    path('login/', login_view, name="login" ),
    path('job/', job_view, name="job" ),
]
