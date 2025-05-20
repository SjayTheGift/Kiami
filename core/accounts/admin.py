from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerSignupForm, CustomUserChangeForm
from .models import User, Profile, Address


class CustomUserAdmin(UserAdmin):
    add_form = CustomerSignupForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active", "is_vendor", "is_customer",)
    list_filter = ("email", "is_staff", "is_active", "is_vendor", "is_customer",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_vendor", "is_customer", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)

admin.site.register(Profile)
admin.site.register(Address)