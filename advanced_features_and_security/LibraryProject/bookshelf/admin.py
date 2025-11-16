from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
  
    list_filter = ("author", "publication_year")

    search_fields = ("title", "author")


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
