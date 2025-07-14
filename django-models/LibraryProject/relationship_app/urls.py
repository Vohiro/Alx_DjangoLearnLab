from django.urls import path
from .views import list_books
#from django.views.generic import DetailView

urlpatterns=[
    path('display-book/', list_books, name='Display Book List'),
    path('library-detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library detail'),
         ]
