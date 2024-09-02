from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from home.models import *


class UserAdmin(BaseUserAdmin):
    list_display = ["username", "email", "password", "first_name", "last_name", "mobile_no", "state", "gender", "role", "created_on", "updated_on"]
    list_filter = ["role"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["username", "first_name", "last_name", "mobile_no", "state", "gender", "role" ]}),
    
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "first_name", "last_name", "mobile_no", "state", "gender", "role", "password1", "password2"]
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "review", "created_on", "updated_on"]
