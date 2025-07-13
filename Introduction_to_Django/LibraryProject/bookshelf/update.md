# Update Book Title

This document details the Python command used to update the title of the "1984" book to "Nineteen Eighty-Four" and save the changes.

## Python Command to Update Book Title

This is the Python code executed within the Django shell (`python manage.py shell`).

```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book instance with the title '1984'.
# IMPORTANT: If you have multiple books titled '1984', you might need to retrieve
# by a more specific identifier like its primary key (ID) if known:
# book_to_update = Book.objects.get(id=YOUR_BOOK_ID)
try:
    book_to_update = Book.objects.get(title='1984')
except Book.DoesNotExist:
    print("Book with title '1984' not found. It might already be 'Nineteen Eighty-Four'.")
    # If the book might already be updated, you could try fetching it by the new title
    book_to_update = Book.objects.get(title='Nineteen Eighty-Four')
    print("Found book with title 'Nineteen Eighty-Four'. Proceeding to verify/re-update.")


# Update the title attribute
book_to_update.title = 'Nineteen Eighty-Four'

# Save the changes to the database
book_to_update.save()

# Verify the updated title (you would typically print this in the shell)
print(book_to_update.title)
# Expected output: Nineteen Eighty-Four