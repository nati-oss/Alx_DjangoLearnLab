# LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView  # must be present
from .models import Book, Library           # must include Library exactly

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # must match exactly
    context_object_name = 'library'                        # must be 'library'
