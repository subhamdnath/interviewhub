from rest_framework import serializers
from home.api_view import *
from home.models import *

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = "__all__"