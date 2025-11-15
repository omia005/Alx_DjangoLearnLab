from django.shortcuts import render
from ./models.py import Library, Book, Author, Librarian

# Create your views here.
def list_books(request):
  books = Book.objects.all()
  context = {"Books":books}
  
  

return render(request, "relationship_app/list_books.html", context)
