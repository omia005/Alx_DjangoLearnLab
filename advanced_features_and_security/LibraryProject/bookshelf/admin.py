from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy



# View Books (requires can_view)
class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    permission_required = "bookshelf.can_view"


# Create Book (requires can_create)

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author", "published_year"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")
    permission_required = "bookshelf.can_create"


# Edit Book (requires can_edit)

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ["title", "author", "published_year"]
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")
    permission_required = "bookshelf.can_edit"



# Delete Book (requires can_delete)

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")
    permission_required = "bookshelf.can_delete"

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
