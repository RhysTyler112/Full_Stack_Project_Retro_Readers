from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Books
from .utils import get_or_create_cart, migrate_session_to_db_cart

def bag_contents(request):
    """
    Context processor for bag contents using database cart
    """
    # Migrate any existing session cart to database
    migrate_session_to_db_cart(request)
    
    # Get cart from database
    cart = get_or_create_cart(request)
    
    bag_items = []
    total = Decimal('0.00')
    product_count = 0

    for cart_item in cart.items.all():
        item_total = cart_item.get_total_price()
        total += item_total
        product_count += cart_item.quantity
        
        bag_items.append({
            'item_id': cart_item.book.isbn,
            'quantity': cart_item.quantity,
            'book': cart_item.book,
            'format': cart_item.format,
            'price': cart_item.get_price(),
            'total_price': item_total,
        })

    # Calculate delivery
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    
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