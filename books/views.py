from django.shortcuts import render, redirect
from .models import Books

# Create your views here.

def book_list(request):
    """A view that displays all books, including sorting and search queries"""
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, "books/books.html", context)