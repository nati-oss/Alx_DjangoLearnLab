from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic import DetailView

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
