# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


# APITestCase is a specialized TestCase class for testing DRF APIs.
class BookAPITests(APITestCase):

    def setUp(self):
        """
        Set up the necessary data and a client for testing.
        This method runs before every single test case.
        """
        # Create a test user for authenticated requests.
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create two authors and some books for testing.
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George R.R. Martin')

        self.book1 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', publication_year=1997, author=self.author1)
        self.book2 = Book.objects.create(title='Harry Potter and the Chamber of Secrets', publication_year=1998, author=self.author1)
        self.book3 = Book.objects.create(title='A Game of Thrones', publication_year=1996, author=self.author2)
        self.book4 = Book.objects.create(title='A Clash of Kings', publication_year=1998, author=self.author2)


    # ----- PERMISSION TESTS -----
    def test_unauthenticated_user_cannot_create_book(self):
        """
        Ensure unauthenticated users cannot create books.
        """
        data = {'title': 'New Book', 'publication_year': 2024, 'author': self.author1.id}
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unauthenticated_user_cannot_update_book(self):
        """
        Ensure unauthenticated users cannot update books.
        """
        data = {'title': 'Updated Title'}
        response = self.client.put(reverse('book-update', args=[self.book1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """
        Ensure an authenticated user can create a book.
        """
        self.client.force_authenticate(user=self.user)
        data = {'title': 'The Hobbit', 'publication_year': 1937, 'author': self.author1.id}
        response = self.client.post(reverse('book-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 5) # Check that the book was added

    def test_authenticated_user_can_update_book(self):
        """
        Ensure an authenticated user can update a book.
        """
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Title', 'publication_year': 2000, 'author': self.author1.id}
        response = self.client.put(reverse('book-update', args=[self.book1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db() # Refresh the object from the database
        self.assertEqual(self.book1.title, 'Updated Title')


    # ----- FUNCTIONALITY TESTS (CRUD, FILTERING, SEARCHING, ORDERING) -----
    def test_list_books_and_check_data(self):
        """
        Test that the list view returns all books and the correct data.
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_book_detail(self):
        """
        Test that retrieving a single book returns the correct data.
        """
        response = self.client.get(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter and the Sorcerer\'s Stone')

    def test_filter_by_publication_year(self):
        """
        Test filtering the book list by publication_year.
        """
        response = self.client.get(reverse('book-list'), {'publication_year': 1998})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        titles = [book['title'] for book in response.data]
        self.assertIn('Harry Potter and the Chamber of Secrets', titles)
        self.assertIn('A Clash of Kings', titles)

    def test_search_by_title(self):
        """
        Test searching the book list by title.
        """
        response = self.client.get(reverse('book-list'), {'search': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        titles = [book['title'] for book in response.data]
        self.assertIn('Harry Potter and the Sorcerer\'s Stone', titles)

    def test_ordering_by_title_ascending(self):
        """
        Test ordering the book list by title in ascending order.
        """
        response = self.client.get(reverse('book-list'), {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_title = response.data[0]['title']
        self.assertEqual(first_title, 'A Clash of Kings')

    def test_ordering_by_title_descending(self):
        """
        Test ordering the book list by title in descending order.
        """
        response = self.client.get(reverse('book-list'), {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_title = response.data[0]['title']
        self.assertEqual(first_title, 'Harry Potter and the Sorcerer\'s Stone')