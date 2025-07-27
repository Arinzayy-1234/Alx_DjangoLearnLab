from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from . models import Book
from .forms import ExampleForm,BookForm

# Create your views here.
# ... (imports) ...

# Secure Data Access: All database interactions (queries, saves, deletes) in this file
# use Django's Object-Relational Mapper (ORM) and Django Forms.
# Why: The ORM inherently uses parameterized queries, which prevents SQL Injection attacks
# by treating all user input as data, not executable code. Django Forms also handle
# automatic input validation and sanitization.

@login_required # Ensures the user is authenticated
@permission_required('bookshelf.can_view', raise_exception=True) # Checks for 'can_view' permission
def book_list(request):
    books = Book.objects.all() # Fetches all Book objects from the database
     # Uses ORM for secure data retrieval
    # Renders the template, passing the 'books' QuerySet to it
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required

def book_edit(request,pk):
    book = get_object_or_404(Book, pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book.list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action' : 'Edit'})


@login_required
@permission_required('bookshelf.can_delete', raise_exception = True)

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book.list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book.list')
    else:
        form = BookForm()
        return render(request,'bookshelf/book_form.html', {'form': form, 'action': 'Create'})


# NEW: View for ExampleForm
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to DB, print to console)
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['your_email']
            print(f"ExampleForm submitted: Name={name}, Email={email}")
            # For this task, we can just redirect or render a success message
            return render(request, 'bookshelf/form_example.html', {'form': form, 'message': 'Form submitted successfully!'})
    else:
        form = ExampleForm() # Create an empty form for GET requests

    # Pass the form to the template
    return render(request, 'bookshelf/form_example.html', {'form': form})