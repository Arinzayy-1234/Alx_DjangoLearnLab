
# Retrieve Book Attributes

This document details the Python command used to retrieve and display all attributes of a specific `Book` instance from the database.

## Python Command to Retrieve and Display Book Attributes

This is the Python code executed within the Django shell (`python manage.py shell`).

```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the specific book instance by its title.
# Replace '1984' with the actual title of the book you created and saved.
book_instance = Book.objects.get(title='1984')

# Display all attributes of the retrieved book
print(f"Book ID: {book_instance.id}")
print(f"Title: {book_instance.title}")
print(f"Author: {book_instance.author}")
print(f"Publication Year: {book_instance.publication_year}")
print(f"ISBN: {book_instance.isbn}")
# Add any other fields you have in your Book model

# Expected output:
# Book ID: 1 
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
# ISBN: 978-0451524935
# (Note: The actual ID will depend on your database, but other details should match what you created)