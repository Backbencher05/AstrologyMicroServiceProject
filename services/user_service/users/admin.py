from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "email",
        "phone_number",
        "full_name",
        "is_astrologer",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active", "is_astrologer", "language", "gender")
    search_fields = ("email", "phone_number", "full_name")
    ordering = ("email",)

    # Fields shown in add/edit page
    fieldsets = (
        (None, {"fields": ("email", "phone_number", "password")}),
        ("Personal Info", {"fields": ("full_name", "gender", "date_of_birth", "language")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
        ("Role", {"fields": ("is_astrologer",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "phone_number", "password1", "password2", "is_staff", "is_active", "is_astrologer"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
