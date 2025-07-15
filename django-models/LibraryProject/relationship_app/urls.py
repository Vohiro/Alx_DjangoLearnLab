from django.urls import path, include
from .views import list_books, LibraryDetailView, LibraryListView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    path('display-book/', list_books, name='Display Book List'),
    path('library-detail/', LibraryListView.as_view(), name='library list detail'),
    path('library-detail/<int:pk>/', LibraryDetailView.as_view(), name='library detail'),
    path('register/', views.RegisterView.as_view(), name='register' ),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationshipp_app/logout.html'), name='logout'), 
         ]
