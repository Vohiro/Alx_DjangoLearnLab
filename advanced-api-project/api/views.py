from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django.contrib import messages

class ListView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


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
