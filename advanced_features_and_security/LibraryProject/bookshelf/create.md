
# Create Book Instance

This document details the Python command used to create a `Book` instance, along with its expected successful output.

## Python Command Used for Creation

This is the Python code executed within the Django shell (`python manage.py shell`).

```python
# Import the Book model
from bookshelf.models import Book

# Create a new Book instance and save it to the database
Book.objects.create(title='1984', author='"George Orwell"', publication_year=1925, isbn='1949')
# Expected output: <Book: The Great Gatsby> or a similar object representation confirming creation.