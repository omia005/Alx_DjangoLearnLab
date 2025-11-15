from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path("/library_details", LibraryDetailView.as_view(), name="library_detail"),
    path("/list_books", list_books.as_view, name="list_books")
]
