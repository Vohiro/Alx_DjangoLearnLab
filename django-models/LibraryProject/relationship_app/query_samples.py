from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author
def book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

#List all books in a Library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

#Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    reuturn library.librarian
