from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields visible in admin user detail page
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "date_of_birth",
                    "profile_photo",
                )
            },
        ),
    )

    # Fields shown when creating new users in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Info",
            {
                "fields": (
                    "date_of_birth",
                    "profile_photo",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
