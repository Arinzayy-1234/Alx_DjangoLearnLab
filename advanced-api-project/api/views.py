# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# This view lists all books. It satisfies the "ListView" requirement.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]    
    # search_fields tells the SearchFilter which model fields to search within.
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

    def get_queryset(self):
        """
        Optionally restricts the returned books to a specific publication year,
        by filtering based on the `publication_year` query parameter in the URL.
        """
        # Get the initial queryset of all books.
        queryset = Book.objects.all()

        # Get the 'publication_year' from the URL's query parameters.
        # It will be None if the parameter is not present.
        publication_year = self.request.query_params.get('publication_year', None)

        # If a publication year is provided, filter the queryset.
        if publication_year is not None:
            # The 'filter' method is used to restrict the queryset.
            queryset = queryset.filter(publication_year=publication_year)

        # Return the final, filtered queryset.
        return queryset


# This view retrieves a single book. It satisfies the "DetailView" requirement.
class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# This view creates a new book. It satisfies the "CreateView" requirement.
class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# This view updates a single book. It satisfies the "UpdateView" requirement.
class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# This view deletes a single book. It satisfies the "DeleteView" requirement.
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]