from django.urls import path
from relationship_app import views
#from django.views.generic import DetailView

urlpatterns=[
    path('display-book/', views.display_book_list, name='Display Book List'),
    path('library-detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library detail'),
         ]
