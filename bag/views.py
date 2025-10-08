from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from books.models import Books
from .utils import (
    get_or_create_cart, 
    add_to_cart, 
    remove_from_cart, 
    update_cart_item_quantity, 
    migrate_session_to_db_cart
)

def view_bag(request):
    """ A view that renders the bag contents page """
    # Migrate any existing session cart to database
    migrate_session_to_db_cart(request)
    return render(request, 'bag/bag.html')

def add_to_bag(request, isbn):
    """Add a quantity of the specified book to the shopping bag"""
    if request.method != 'POST':
        messages.error(request, 'Invalid request method.')
        return redirect('books')
    
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
    except (ValueError, TypeError):
        messages.error(request, 'Please enter a valid quantity.')
        return redirect(request.POST.get('redirect_url', 'books'))

    format = request.POST.get('format')
    redirect_url = request.POST.get('redirect_url', 'books')

    # Validate format is provided
    if not format:
        messages.error(request, 'Please select a format before adding the book to your bag.')
        return redirect(redirect_url)

    # Validate format is valid
    if format not in ['softcover', 'hardcover', 'audiobook']:
        messages.error(request, 'Invalid format selected.')
        return redirect(redirect_url)

    # Add to cart with validation
    success, message = add_to_cart(request, isbn, format, quantity)
    
    if success:
        messages.success(request, message)
    else:
        messages.error(request, message)

    return redirect(redirect_url)

def adjust_bag(request, isbn):
    """Adjust the quantity of the specified book in the shopping bag"""
    if request.method != 'POST':
        messages.error(request, 'Invalid request method.')
        return redirect('view_bag')
    
    try:
        quantity = int(request.POST.get('quantity', 0))
    except (ValueError, TypeError):
        messages.error(request, 'Please enter a valid quantity.')
        return redirect(reverse('view_bag'))

    format = request.POST.get('format')
    
    if not format:
        messages.error(request, 'Format is required.')
        return redirect(reverse('view_bag'))

    # Update cart item quantity
    success, message = update_cart_item_quantity(request, isbn, format, quantity)
    
    if success:
        messages.success(request, message)
    else:
        messages.error(request, message)

    return redirect(reverse('view_bag'))

def remove_from_bag(request, isbn):
    """Remove the specified book format from the shopping bag"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    format = request.POST.get('format')
    
    if not format:
        return JsonResponse({'error': 'Format is required'}, status=400)

    success, message = remove_from_cart(request, isbn, format)
    
    if success:
        messages.success(request, message)
        return HttpResponse(status=200)
    else:
        messages.error(request, message)
        return JsonResponse({'error': message}, status=404)