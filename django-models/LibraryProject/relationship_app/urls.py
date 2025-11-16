from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views

urlpatterns = [
    path("library_details/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("list_books/", views.list_books.as_view, name="list_books"),
    path("register/", views.register.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login" ),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout" ),
]
