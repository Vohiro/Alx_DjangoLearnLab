from django.shortcuts import render
from .models import Library, Book, Author, Librarian
from django.views.generic import DetailView

# Create your views here.

def display_book_list(request):
    """ Retrieves all books and display all book titles and their authors"""
    books = Book.objects.all()
    context = { 'book_list': books }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """ A class based view for displaying list details of a specific library """
    model = Library
    template_name = "relationship_app/library_detail.html"
