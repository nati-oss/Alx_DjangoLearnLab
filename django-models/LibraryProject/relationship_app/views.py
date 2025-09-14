# LibraryProject/relationship_app/views.py  
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render
from django.views.generic import DetailView  # must be present
from .models import Book         # must include Library exactly
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # must match exactly
    context_object_name = 'library'                        # must be 'library'

# 🔹 User Registration View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in the new user right away
            return redirect("list_books")  # redirect to books page or wherever
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# 🔹 User Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# 🔹 User Logout View
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")