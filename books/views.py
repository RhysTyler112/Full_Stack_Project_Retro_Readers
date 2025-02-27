from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Books

# Create your views here.

def book_list(request):
    """A view that displays all books, including sorting and search queries"""
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, "books/books.html", context)

def book_detail(request, isbn):
    """A view that displays the details of a single book using ISBN"""
    book = get_object_or_404(Books, isbn=isbn)
    context = {
        'book': book,
    }
    return render(request, "books/books_detail.html", context)