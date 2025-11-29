from django.db import models

# Create your models here.
#this is the Author model
class Author(models.Model):
  name = models.Charfield(max_length = 100)

#this is the Book model
class Book(models.Model):
  title = models.Charfield(max_length = 200)
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)