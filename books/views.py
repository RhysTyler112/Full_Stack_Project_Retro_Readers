from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F
from .models import Books, Category
from .forms import BookForm

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

@login_required
def add_book(request):
    """Add a book to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('book_detail', args=[form.instance.isbn]))
        else:
            messages.error(request, 'Failed to add book. Please ensure the form is valid.')
    else:
        form = BookForm()
        
    template = 'books/add_book.html'
    context = {
        'form': form,
    }
    
    return render(request, template, context)

@login_required
def edit_book(request, isbn):
    """Edit a book in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    book = get_object_or_404(Books, isbn=isbn)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('book_detail', args=[book.isbn]))
        else:
            messages.error(request, 'Failed to update book. Please ensure the form is valid.')
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.title}')
        
    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }
    
    return render(request, template, context)

@login_required
def delete_book(request, isbn):
    """Delete a book from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    book = get_object_or_404(Books, isbn=isbn)
    book.delete()
    messages.success(request, 'Book deleted!')
    return redirect(reverse('books'))