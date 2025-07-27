from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from . models import Book
from . forms import BookForm

# Create your views here.

@login_required # Ensures the user is authenticated
@permission_required('bookshelf.can_view', raise_exception=True) # Checks for 'can_view' permission
def book_list(request):
    books = Book.objects.all() # Fetches all Book objects from the database
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
