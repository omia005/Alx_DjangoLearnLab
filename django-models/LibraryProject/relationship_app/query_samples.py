import django
import os
from ./models.py import Author, library, Librarian, Book

def query_books_by_author(author_name):
  try:
    author = Author.objects.get(author_name)
    books = Book.objects.filter(author=author)
    print (f"\n the books by {author}:")
    for book in books:
      print(f"\n {book.title}")

  except Author.DoesNotExist:
      print(f"No author found with name: {author_name}")

def list_books_in_library(library_name):
  try:
    library = library.objects.get(name=library.name)
    books = library.books.all()
    for book in books:
      print(f"{book.title}")

  except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

def retrieve_librarian(library_name):
  try:
    library = library.objects.get(name=library.name)
    librarian = librarian.objects.get(library=library)
    print(f"librarian for {library.name} Library is {librarian}")


if __name__ = __main__ :
  query_books_by_author()
  list_books_in_library()
  retrieve_librarian()

  
     
