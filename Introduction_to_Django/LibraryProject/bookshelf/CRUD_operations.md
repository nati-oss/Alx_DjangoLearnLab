# Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Retrieve
Book.objects.all()

# Update
book.title = "Nineteen Eighty-Four"
book.save()
book

# Delete
book.delete()
Book.objects.all()
