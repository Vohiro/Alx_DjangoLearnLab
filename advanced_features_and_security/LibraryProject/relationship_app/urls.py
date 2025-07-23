from django.urls import path, include
from .views import list_books, LibraryDetailView, LibraryListView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path('display-book/', list_books, name='display-book-list'),
    path('library-detail/', LibraryListView.as_view(), name='library-list-detail'),
    path('library-detail/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register' ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationshipp_app/logout.html'), name='logout'),
    path('admin-only/', views.admin_view, name='admin_view'),
    path('librarian-only/', views.librarian_view, name='librarian_view'),
    path('member-only/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete-book')
         ]
