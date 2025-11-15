from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path("/library_details", views.LibraryDetailView.as_view(), name="library_detail"),
    path("/list_books", views.list_books, name="list_books"),
]
