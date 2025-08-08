from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django.contrib import messages
from django_filters.rest_framework import DjangoFilterBackend

class ListView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enabling filtering, searching and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year'] #filtering by fields
    search_fields = ['title', 'author'] # search setup
    ordering_fields = ['title','publication_year'] # ordering setup
    ordering = ['title'] # default ordering 

class DetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def form_valid(self, form):
        messages.success(self.request, 'Book created successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'There were errors in the form. Please correct them.')
        return super().form_invalid(form)

class UpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def form_valid(self, form):
        messages.success(self.request, 'Book created successfully!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'There were errors in the form. Please correct them.')
        return super().form_invalid(form)


class DeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
