#Retrieve the book created

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication

# Expected Output: ('1984', 'George Orwell', 1949)
