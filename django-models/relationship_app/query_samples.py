import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1️⃣ Query all books by a specific author
    try:
        author = Author.objects.get(name="J.K. Rowling")
        print(f"Books by {author.name}:")
        for book in author.books.all():
            print("-", book.title)
    except Author.DoesNotExist:
        print("Author not found.")

    # 2️⃣ List all books in a library
    try:
        library = Library.objects.get(name="Central Library")
        print(f"\nBooks in {library.name}:")
        for book in library.books.all():
            print("-", book.title)
    except Library.DoesNotExist:
        print("Library not found.")

    # 3️⃣ Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print("Librarian not found for this library.")

if __name__ == "__main__":
    run_queries()
