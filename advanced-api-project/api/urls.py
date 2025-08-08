from django.urls import path
from .views import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

urlpatterns = [
    path('/books/', ListView.as_view(), name='book_list'),
    path('/books/<int:pk>/', DetailView.as_view(), name='book_detail'),
    path('/books/create/<int:pk>', CreateView.as_view(), name='book_create'),
    path('/books/update/<int:pk>', UpdateView.as_view(), name='book_update'),
    path('/books/delete/<int:pk>', DeleteView.as_view(), name='book_delete'),
]
