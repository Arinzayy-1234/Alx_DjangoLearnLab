# Delete Book Instance

This document details the Python command used to delete a specific `Book` instance from the database and confirms its removal.

## Python Command to Delete Book

This is the Python code executed within the Django shell (`python manage.py shell`).

```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book instance you want to delete.
# Assuming 'Nineteen Eighty-Four' is the title of the book you previously created/updated.
# If you created multiple, or have others, you might want to retrieve by ID:
# book = Book.objects.get(id=YOUR_BOOK_ID_HERE)
try:
    book = Book.objects.get(title='Nineteen Eighty-Four')
except Book.DoesNotExist:
    print("Book 'Nineteen Eighty-Four' not found. It might have already been deleted or never existed.")
    # If the book is not found, the deletion part won't execute.
    # For documentation, you'd show a successful deletion path assuming it exists.

# Perform the deletion.
# The .delete() method returns a tuple: (number_of_objects_deleted, dictionary_of_deleted_object_types)
deletion_result = book.delete()

# Confirm deletion by trying to retrieve all books again
remaining_books = Book.objects.all()

print(f"Deletion result: {deletion_result}")
print(f"Books remaining in database: {remaining_books}")

# Expected output:
# Deletion result: (1, {'bookshelf.Book': 1})
# Books remaining in database: <QuerySet []>
# (If there were other books in your database, the QuerySet would list them. If this was the only book, the QuerySet will be empty.)