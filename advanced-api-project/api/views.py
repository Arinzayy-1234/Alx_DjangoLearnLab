# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# This view handles listing all books and creating a new book.
# It inherits from generics.ListCreateAPIView, which combines
# the logic of a ListAPIView and a CreateAPIView.
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allows anyone to read, but only authenticated users to create.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Note: DRF's generic views automatically handle validation
    # by calling the serializer's .is_valid() method on POST requests.
    # Your custom validation in BookSerializer.validate_publication_year
    # will be run automatically.

# This view handles retrieving, updating, and deleting a single book.
# It inherits from generics.RetrieveUpdateDestroyAPIView.
class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allows anyone to read, but only authenticated users can update or delete.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Note: The UpdateAPIView part of this class will also use your
    # serializer's validation logic to check for a valid publication_year
    # when a PUT or PATCH request is made.