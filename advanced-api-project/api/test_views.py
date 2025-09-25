from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    """Tests for Book API endpoints using APITestCase"""

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a book
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=2001,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    # ---------- CRUD Tests ----------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter", str(response.data))

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter")

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "New Book", "publication_year": 2020, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Harry Potter Updated", "publication_year": 2001, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Harry Potter Updated")

    def test_delete_book(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # ---------- Filtering / Searching / Ordering ----------

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "Harry Potter"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Rowling"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Harry Potter", str(response.data))

    def test_order_books(self):
        # Add another book
        Book.objects.create(title="A Book", publication_year=1990, author=self.author)
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First book should be the oldest
        self.assertEqual(response.data[0]["title"], "A Book")
