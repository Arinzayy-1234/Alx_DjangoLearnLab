# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# This view lists all books.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allows anyone to read (list).
    permission_classes = [IsAuthenticatedOrReadOnly]

# This view retrieves a single book by ID.
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allows anyone to read (retrieve).
    permission_classes = [IsAuthenticatedOrReadOnly]

# This view allows new books to be created.
class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can create books.
    permission_classes = [IsAuthenticated]

# This view allows a single book to be updated.
class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update books.
    permission_classes = [IsAuthenticated]

# This view allows a single book to be deleted.
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can delete books.
    permission_classes = [IsAuthenticated]