

def run():
    """
    This function is used to run the query samples.
    It creates an author and two books, then retrieves and prints the titles of the books associated with that author.
    """
    print("Running query samples...")

    from relationship_app.models import Author, Book, Library, Librarian

    jk_rowling_author,created_author = Author.objects.get_or_create(name = 'J.K. Rowlingj')

    book_1, created_book1 = Book.objects.get_or_create(title = 'Harry Potter and the philosopher\'s stone', author =  jk_rowling_author)

    book_2 , created_book2 = Book.objects.get_or_create(title = 'Harry Potter and the chamber of secrets', author = jk_rowling_author)


    books_of_jk_rowling_author = jk_rowling_author.books.all()

    for  books in books_of_jk_rowling_author:
        print(books.title)

    veritas_library = Library.objects.create(name = 'Veritas Library')
    veritas_library.books.add(book_1,book_2)

    veritas_books = veritas_library.books.all()

    for book in veritas_books:
        print(f'Vertias Library has the book: {book.title}')

    librarian_1 = Librarian.objects.create(name = 'Arinzayyy', library = veritas_library)

    veritas_librarians = veritas_library.librarians.all()

    for librarian in veritas_librarians:
        print(f'Veritas library has the librarian: {librarian.name}')