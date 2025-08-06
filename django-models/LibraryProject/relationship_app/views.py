from django.shortcuts import render
from relationship_app.models import Book, Author,Librarian
from .models import Library
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login,logout

# Create your views here.

def list_books(request):
    # retrieve all books
    all_books = Book.objects.all()
    context = {'books' : all_books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):

    model = Library
    template_name = 'relationship_app/library_detail.html'
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        library = self.get_object()
        return context
        

class SignupView(CreateView):

    template_name = 'relationship_app/register.html'

    form_class = UserCreationForm

    success_url = reverse_lazy('login')

    def form_valid(self, form):
        return super().form_valid(form)
        login(self.request, self.object)
        return response
    
