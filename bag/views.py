from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from books.models import Books

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, isbn):
    """Add a quantity of the specified book to the shopping bag"""
    book = get_object_or_404(Books, isbn=isbn)
    quantity = int(request.POST.get('quantity'))
    format = request.POST.get('format')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if isbn in bag:
        if format in bag[isbn]:
            bag[isbn][format] += quantity
        else:
            bag[isbn][format] = quantity
    else:
        bag[isbn] = {format: quantity}

    request.session['bag'] = bag
    messages.success(request, f'Added {book.title} ({format}) to your bag')

    return redirect(redirect_url)