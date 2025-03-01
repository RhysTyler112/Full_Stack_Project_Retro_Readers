from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Books

# Create your views here.

def book_list(request):
    """A view that displays all books, including sorting and search queries"""
    books = Books.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query) 
            books = books.filter(queries)
    
    context = {
        'books': books,
        'search_term': query,
    }
    
    return render(request, "books/books.html", context)

def book_detail(request, isbn):
    """A view that displays the details of a single book using ISBN"""
    book = get_object_or_404(Books, isbn=isbn)
    context = {
        'book': book,
    }
    return render(request, "books/books_detail.html", context)