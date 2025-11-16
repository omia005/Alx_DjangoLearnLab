from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from . import views

urlpatterns = [
    path("library_details/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("list_books/", views.list_books, name="list_books"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
