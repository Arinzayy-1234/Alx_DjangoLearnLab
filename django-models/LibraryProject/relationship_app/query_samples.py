
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_1 = Author.objects.create(name = 'J.K. Rowlingj')

book_1 = Book.objects.create(title = 'Harry Potter and the philosopher\'s stone', author = Author.objects.get(name = 'J.K. Rowlingj'))

book_2 = Book.objects.create(title = 'Harry Potter and the chamber of secrets', author = Author.objects.create(name = 'J.K. Rowlingj'))


books_of_author_1 = author_1.books.all()

for  books in books_of_author_1:
    print(books.title)