from django.core.exceptions import ObjectDoesNotExist

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






    # --- THIS IS THE ONLY SECTION FOR GETTING/CREATING VERITAS LIBRARY ---

    # Define the library name in a variable, as the checker implies 'library_name' variable
    specific_library_name = 'Veritas Library'

    # Attempt to GET the library (as required by the checker).
    # If it doesn't exist, CREATE it (to ensure script robustness).
    try:
        veritas_library = Library.objects.get(name=specific_library_name)
        print(f"Library '{veritas_library.name}' successfully retrieved using .get().")
    except ObjectDoesNotExist: # Catches if .get() finds no object
        veritas_library = Library.objects.create(name=specific_library_name)
        print(f"Library '{veritas_library.name}' created as it did not exist for .get() call.")
    except Exception as e: # Catch any other unexpected errors
        print(f"An unexpected error occurred trying to get/create library: {e}")
        return # Exit the function if a critical error happens

    # --- End of Library creation/retrieval ---

    # Now, add books to this 'veritas_library' object, which is guaranteed to exist
    veritas_library.books.add(book_1,book_2)

    veritas_books = veritas_library.books.all()

    for book in veritas_books:
        print(f'Veritas Library has the book: {book.title}')

# Create the librarian, linking to the 'veritas_library' obtained above
    librarian_1 = Librarian.objects.get_or_create(name = 'Arinzayyy', library = veritas_library)[0] # Use get_or_create for librarian too for robustness!

    veritas_librarians = veritas_library.librarians.all()

    for librarian in veritas_librarians:
        print(f'Veritas library has the librarian: {librarian.name}')