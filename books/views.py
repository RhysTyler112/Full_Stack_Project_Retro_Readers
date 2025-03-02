from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, F
from .models import Books, Category

def book_list(request):
    """A view that displays all books, including sorting and search queries"""
    books = Books.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                books = books.annotate(lower_title=F('title'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            elif sortkey == 'price':
                sortkey = 'price_softcover'  # Default to softcover price for sorting

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('books'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query) 
            books = books.filter(queries)
    
        if 'format' in request.GET:
            format_filter = request.GET['format']
            if format_filter == 'softcover':
                books = books.filter(price_softcover__isnull=False)
            elif format_filter == 'hardcover':
                books = books.filter(price_hardcover__isnull=False)
            elif format_filter == 'audiobook':
                books = books.filter(price_audiobook__isnull=False)
        
    current_sorting = f'{sort}_{direction}'
        
    context = {
        'books': books,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, "books/books.html", context)

def book_detail(request, isbn):
    """A view that displays the details of a single book using ISBN"""
    book = get_object_or_404(Books, isbn=isbn)
    context = {
        'book': book,
    }
    return render(request, "books/books_detail.html", context)