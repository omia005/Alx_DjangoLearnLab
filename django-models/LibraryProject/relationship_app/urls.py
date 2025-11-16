from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path("library_details/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("list_books/", views.list_books.as_view, name="list_books"),
    path("register/", views.register.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login" ),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout" ),
    path('admin-dashboard/', admin_view.as_view(), name='admin_view'),
    path('librarian-dashboard/', librarian_view.as_view(), name='librarian_view'),
    path('member-dashboard/', member_view.as_view(), name='member_view'),
    path('books/add/', add_book.as_view(), name='add_book'),
    path('books/edit/', edit_book.as_view, name='edit_book'),
    path('books/delete/', delete_book.as_view(), name='delete_book'),
]
