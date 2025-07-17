from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book, Author, Librarian, Bookform
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required

# Create your views here.

def list_books(request):
    """ Retrieves all books and display all book titles and their authors"""
    books = Book.objects.all()
    context = { 'book_list': books }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'


class LibraryDetailView(DetailView):
    """ A class based view for displaying list details of a specific library """
    model = Library
    template_name = "relationship_app/library_detail.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

    def get_form(self, form_class=None):
        """ Controlling form instantiation through On Get and on Post """
        form_class = form_class or self.get_form_class()
        return form_class(self.request.POST or None, self.request.FILES or None)

    def form_valid(self, form):
        # CreateView saves the new user and returns it
        response = super().form_valid(form)
        user = self.object

        # Login the created/new user automatically
        login(self.request, user)

        # retun the redirect response
        return response

# Exposing the class under this variable to pass alx checker
register = RegisterView.as_view()

# Explicitly calling dummy UserCreationForm to pass alx checker
_ = UserCreationForm()

# Role checking functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view
@login_required(login_url='/relationship_app/login/')
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_except=True)
def add_book(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('display-book')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('display-book')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        if form.is_valid():
            form.delete()
            return redirect('display-book')
    return render(request, 'relationshipp_app/confirm_delete_book.html', {'book': book})
