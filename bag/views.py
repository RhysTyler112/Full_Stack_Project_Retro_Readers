from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
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

    # Ensure a format is selected
    if not format:
        messages.error(request, 'Please select a format before adding the book to your bag.')
        return redirect(redirect_url)

    bag = request.session.get('bag', {})

    if isbn in bag:
        if format in bag[isbn]:
            bag[isbn][format] += quantity
        else:
            bag[isbn][format] = quantity
    else:
        bag[isbn] = {format: quantity}
        messages.success(request, f'Added {book.title} ({format}) to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, isbn):
    """Adjust the quantity of the specified book in the shopping bag"""
    book = get_object_or_404(Books, isbn=isbn)
    quantity = int(request.POST.get('quantity'))
    format = request.POST.get('format')
    bag = request.session.get('bag', {})

    if format:
        if quantity > 0:
            bag[isbn][format] = quantity
            messages.success(request, f'Updated {book.title} ({format}) quantity to {quantity}')
        else:
            del bag[isbn][format]
            if not bag[isbn]:
                bag.pop(isbn)
            messages.success(request, f'Removed {book.title} ({format}) from your bag')
    else:
        if quantity > 0:
            bag[isbn] = quantity
            messages.success(request, f'Updated {book.title} quantity to {quantity}')
        else:
            bag.pop(isbn)
            messages.success(request, f'Removed {book.title} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, isbn):
    """Remove the specified book format from the shopping bag"""
    book = get_object_or_404(Books, isbn=isbn)
    format = request.POST.get('format')
    bag = request.session.get('bag', {})

    try:
        if isbn in bag:
            if format and format in bag[isbn]:
                del bag[isbn][format]
                if not bag[isbn]:
                    bag.pop(isbn)
                messages.success(request, f'Removed {book.title} ({format}) from your bag')
            else:
                messages.error(request, f'Format {format} not found in your bag for {book.title}')
            request.session['bag'] = bag
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)