from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication tests
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create sample books
        self.book1 = Book.objects.create(
            title="Django Unleashed",
            author="Andrew Pinkham",
            publication_year=2015
        )
        self.book2 = Book.objects.create(
            title="Learning Python",
            author="Mark Lutz",
            publication_year=2013
        )
        self.book3 = Book.objects.create(
            title="Python Crash Course",
            author="Eric Matthes",
            publication_year=2019
        )

        self.list_url = reverse("book-list")  # Ensure you named your ListView route "book-list"
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])

    # ---------------------------------------
    # CRUD TESTS
    # ---------------------------------------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "New Book",
            "author": "Someone",
            "publication_year": 2024
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "Unknown",
            "publication_year": 2024
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_single_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django Unleashed")

    def test_update_book(self):
        self.client.login(username="testuser", password="password123")

        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url(self.book1.id), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.delete(self.detail_url(self.book1.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ---------------------------------------
    # FILTERING, SEARCHING & ORDERING TESTS
    # ---------------------------------------

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Mark Lutz"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Mark Lutz")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # book2 and book3 match
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_order_books_descending(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    # ---------------------------------------
    # AUTHENTICATION / PERMISSION TESTS
    # ---------------------------------------

    def test_unauthenticated_user_cannot_create(self):
        data = {"title": "Hacker Book", "author": "Hacker", "publication_year": 2024}
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_create(self):
        self.client.login(username="testuser", password="password123")

        data = {"title": "Legit Book", "author": "Author", "publication_year": 2024}
        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
