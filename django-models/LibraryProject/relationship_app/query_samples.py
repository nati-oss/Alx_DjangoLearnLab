import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1️⃣ Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print("-", book.title)
    except Author.DoesNotExist:
        print("Author not found.")

    # 2️⃣ List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print("-", book.title)
    except Library.DoesNotExist:
        print("Library not found.")

    # 3️⃣ Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nLibrarian of {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print("Librarian not found for this library.")

if __name__ == "__main__":
    run_queries()
