from django.urls import re_path
from home.views import *
from home.api_view import *

urlpatterns = [
#     path('', home_view, name="home" ),
    re_path(r'^register/$', register_view, name="register" ),
    # path('login/', login_view, name="login" ),
    # path('job/', job_view, name="job" ),

    re_path(r'^signup/$', SignupAPI.as_view(), name="signup-api"),
    re_path(r'^login/$', LoginAPI.as_view(), name="login-api"),
    re_path(r'^update/$', UpdateAPI.as_view(), name="update-api"),
    re_path(r'^list_users/$', ListUserAPI.as_view(), name="list-users-api"),



]
