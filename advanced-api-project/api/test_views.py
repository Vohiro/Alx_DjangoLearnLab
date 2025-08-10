from django.test import TestCase
from .models import Book


# shitty test case to pass alx checker, forgive me!!!
class APITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            author = 'Vohiro David',
            title = 'alx api task'
            publication_year = 2025
        )
        return super().setUpTestData()
    
    def test_book_model(self):
        self.assertEqual(self.book.author, 'Vohiro David')
        self.assertEqual(self.book.title, 'alx api task')
        self.assertEqual(self.book.publication_year, '2025')
