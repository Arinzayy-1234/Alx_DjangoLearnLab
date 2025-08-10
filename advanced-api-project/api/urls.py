# api/urls.py
from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDestroy

urlpatterns = [
    # This path handles both listing all books (GET) and creating a new book (POST).
    path('books/', BookListCreate.as_view(), name='book-list-create'),

    # This path handles retrieving, updating, and deleting a specific book.
    # The <int:pk> part captures the primary key (ID) from the URL.
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-detail'),
]