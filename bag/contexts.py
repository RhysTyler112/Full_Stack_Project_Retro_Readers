from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Books

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, formats in bag.items():
        book = get_object_or_404(Books, isbn=item_id)
        for format, quantity in formats.items():
            # Determine the price based on the format
            if format == 'softcover':
                price = book.price_softcover
            elif format == 'hardcover':
                price = book.price_hardcover
            elif format == 'audiobook':
                price = book.price_audiobook
            else:
                price = 0  # Default to 0 if no valid format is found

            total += quantity * price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'book': book,
                'format': format,
                'price': price,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context