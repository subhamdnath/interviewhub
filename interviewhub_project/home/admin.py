from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from home.models import MyUser


class UserAdmin(BaseUserAdmin):
    list_display = ["full_name", "email", "phone_number", "state", "gender", "role", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["full_name", "phone_number", "state", "gender", "role" ]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["full_name", "email", "phone_number", "state", "gender", "role", "password1", "password2", "is_admin"]
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(MyUser, UserAdmin)