from bookshelf.models import Book

# Retrieve the book we created using get
book = Book.objects.get(title="1984")
book
# Expected output: <Book: 1984 by George Orwell (1949)>
