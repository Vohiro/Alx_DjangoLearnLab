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
    path('/books/<int:pk>/create', CreateView.as_view(), name='book_create'),
    path('/books/<int:pk>/update', UpdateView.as_view(), name='book_update'),
    path('/books/<int:pk>/delete', DeleteView.as_view(), name='book_delete'),
]
