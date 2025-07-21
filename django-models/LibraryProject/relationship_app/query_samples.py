

def run():
    """
    This function is used to run the query samples.
    It creates an author and two books, then retrieves and prints the titles of the books associated with that author.
    """
    print("Running query samples...")

    from relationship_app.models import Author, Book, Library, Librarian

    author_1,created_author = Author.objects.get_or_create(name = 'J.K. Rowlingj')

    book_1, created_book1 = Book.objects.get_or_create(title = 'Harry Potter and the philosopher\'s stone', author =  author_1)

    book_2 , created_book2 = Book.objects.get_or_create(title = 'Harry Potter and the chamber of secrets', author = author_1)


    books_of_author_1 = author_1.books.all()

    for  books in books_of_author_1:
        print(books.title)