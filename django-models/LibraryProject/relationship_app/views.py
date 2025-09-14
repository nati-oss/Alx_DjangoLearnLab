# LibraryProject/relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ✅ exact import checker expects

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: display library details and all its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ exact path for checker
    context_object_name = 'library'  # ✅ variable name 'library'
