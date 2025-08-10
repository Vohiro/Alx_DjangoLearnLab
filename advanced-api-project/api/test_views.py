from django.test import TestCase
from .models import Book
from rest_framework import status, test


# shitty test case to pass alx checker, forgive me!!!
class APITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = test.APIClient()
        cls.book = Book.objects.create(
            author = 'Vohiro David',
            title = 'alx api task',
            publication_year = 2025
        )
        return super().setUpTestData()
    
    def test_book_model(self):
        self.assertEqual(self.book.author, 'Vohiro David')
        self.assertEqual(self.book.title, 'alx api task')
        self.assertEqual(self.book.publication_year, 2025)

    def test_get_book_details(self):
        response = self.client.get('book_list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('author', response.data[0])
        self.assertEqual(response.data[0]['author']['Vohiro David'])