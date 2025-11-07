from bookshelf.models import Book

book = Book.objects.create(
    title="Things Fall Apart",
    author="Chinua Achebe",
    published_year=1958
)
