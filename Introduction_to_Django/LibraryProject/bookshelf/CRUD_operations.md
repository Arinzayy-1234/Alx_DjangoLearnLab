# CREATE OPERATION
>>> from bookshelf.models import Book
>>> book1 = Book.objects.create(title='The Old Man and the Sea', author='Ernest Hemingway', publication_year=1952, isbn='978-0684801223')
>>> book2 = Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee', publication_year=1960, isbn='978-0446310789')
>>> book3 = Book.objects.create(title='Pride and Prejudice', author='Jane Austen', publication_year=1813, isbn='978-0141439518')
>>> print(book1)
BookID 1 Book: The Old Man and the Sea, Author: Ernest Hemingway, Year: 1952
>>> print(book2)
BookID 2 Book: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
>>> print(book3)
BookID 3 Book: Pride and Prejudice, Author: Jane Austen, Year: 1813
>>>
 # Read (Retrieve) Operation
 >>> # Retrieve all books
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(book)
...
BookID 1 Book: The Old Man and the Sea, Author: Ernest Hemingway, Year: 1952
BookID 2 Book: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
BookID 3 Book: Pride and Prejudice, Author: Jane Austen, Year: 1813
>>>
>>> # Retrieve a specific book by its ID (adjust ID as per your database)
>>> single_book = Book.objects.get(id=2)
>>> print(f"Retrieved: {single_book.title} by {single_book.author}")
Retrieved: To Kill a Mockingbird by Harper Lee
>>>
# Update Operation
>>> # Retrieve the book to update (e.g., 'To Kill a Mockingbird')
>>> book_to_update = Book.objects.get(title='To Kill a Mockingbird')
>>> book_to_update.publication_year = 1961 # Update the publication year
>>> book_to_update.save() # Save the changes
>>> print(f"Updated book title: {book_to_update.title}, new year: {book_to_update.publication_year}")
Updated book title: To Kill a Mockingbird, new year: 1961
>>>
#  Delete Operation
>>> # Retrieve the book to delete (e.g., 'Pride and Prejudice')
>>> book_to_delete = Book.objects.get(title='Pride and Prejudice')
>>> deletion_result = book_to_delete.delete() # Perform the deletion
>>> print(f"Deletion result: {deletion_result}")
Deletion result: (1, {'bookshelf.Book': 1})
>>>
>>> # Confirm deletion by listing all remaining books
>>> remaining_books = Book.objects.all()
>>> for book in remaining_books:
...     print(book)
...
BookID 1 Book: The Old Man and the Sea, Author: Ernest Hemingway, Year: 1952
BookID 2 Book: To Kill a Mockingbird, Author: Harper Lee, Year: 1961
>>>
