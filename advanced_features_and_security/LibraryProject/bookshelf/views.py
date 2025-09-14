from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookSearchForm  # if you have a search form

# DEBUG=False disables detailed error pages to prevent information leakage
# SECURE_BROWSER_XSS_FILTER enables browser-level XSS protection
# CSRF_COOKIE_SECURE ensures CSRF cookies are only sent over HTTPS
# SESSION_COOKIE_SECURE ensures session cookies are only sent over HTTPS
# CSP settings restrict content loading to trusted sources to reduce XSS risk


# View book list (requires can_view)
@permission_required("bookshelf.can_view", raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, "bookshelf/list_books.html", {"books": books})

# Add book (requires can_create)
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})

# Edit book (requires can_edit)
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form})

# Delete book (requires can_delete)
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})

["book_list"]

def search_books(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        title = form.cleaned_data.get("title")
        # Safe ORM filtering prevents SQL injection
        books = Book.objects.filter(title__icontains=title)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})