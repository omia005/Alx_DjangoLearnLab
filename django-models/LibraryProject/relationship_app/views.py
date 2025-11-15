from django.shortcuts import render
from django.http import HttpResponse
from ./models.py import Library, Book, Author, Librarian

# Create your views here.
def book_list(request):
  books = Book.objects.all
  book_list_text = "Book List:\n\n"
    
  for book in books:
        book_list_text += f"- {book.title} by {book.author.name}\n"

return HttpResponse(book_list_text, content_type= "text/plain")
