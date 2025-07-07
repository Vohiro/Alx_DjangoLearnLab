#Create a Book instance

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
Book.objects.all()

# Expected Output: <QuerySet [<Book: Book object (1)>]>


#Retrieve the book created

```python
from bookshelf.models import Book
book.title, book.author, book.publication

# Expected Output: ('1984', 'George Orwell', 1949)


# Update the title of the book

```python
from bookshelf.models import Book
book.title = "Nineteen Eighty-Four"
book.save()
book.title

# Expected Output = 'Nineteen Eight-Four'


#Delete book created

```python
from bookshelf.models import Book
book.delete()

# Expected Output: (1, {'bookshelf.Book': 1})
