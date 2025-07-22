from django.shortcuts import render
from relationship_app.models import Book, Author,Librarian
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.

def AllBooks(request):
    # retrieve all books
    all_books = Book.objects.all()
    context = {'books' : all_books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryView(DetailView):

    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        library = self.get_object()
        return context
        