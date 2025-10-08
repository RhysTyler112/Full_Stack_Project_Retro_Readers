from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from .models import Cart, CartItem
from books.models import Books


def get_or_create_cart(request):
    """
    Get or create cart for current user/session
    """
    if request.user.is_authenticated:
        # For logged-in users, get cart by user
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # If user was previously anonymous, merge their session cart
        if hasattr(request, 'session') and request.session.session_key:
            try:
                session_cart = Cart.objects.get(session_key=request.session.session_key)
                # Merge session cart items into user cart
                for item in session_cart.items.all():
                    try:
                        # Try to find existing item with same book and format
                        existing_item = cart.items.get(book=item.book, format=item.format)
                        existing_item.quantity += item.quantity
                        existing_item.save()
                    except CartItem.DoesNotExist:
                        # Create new item in user cart
                        item.cart = cart
                        item.save()
                
                # Delete the session cart
                session_cart.delete()
            except Cart.DoesNotExist:
                pass
                
    else:
        # For anonymous users, get cart by session key
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    
    return cart


def add_to_cart(request, isbn, format, quantity):
    """
    Add item to cart with validation
    """
    try:
        book = Books.objects.get(isbn=isbn)
    except Books.DoesNotExist:
        return False, "Book not found"
    
    # Validate format and price
    if format == 'softcover' and book.price_softcover is None:
        return False, f"Softcover format not available for {book.title}"
    elif format == 'hardcover' and book.price_hardcover is None:
        return False, f"Hardcover format not available for {book.title}"
    elif format == 'audiobook' and book.price_audiobook is None:
        return False, f"Audiobook format not available for {book.title}"
    elif format not in ['softcover', 'hardcover', 'audiobook']:
        return False, "Invalid format selected"
    
    cart = get_or_create_cart(request)
    
    try:
        # Try to get existing cart item
        cart_item = cart.items.get(book=book, format=format)
        cart_item.quantity += quantity
        cart_item.save()
        action = "updated"
    except CartItem.DoesNotExist:
        # Create new cart item
        cart_item = CartItem.objects.create(
            cart=cart,
            book=book,
            format=format,
            quantity=quantity
        )
        action = "added"
    
    return True, f"{action.title()} {book.title} ({format}) in your cart"


def remove_from_cart(request, isbn, format):
    """
    Remove item from cart
    """
    try:
        book = Books.objects.get(isbn=isbn)
    except Books.DoesNotExist:
        return False, "Book not found"
    
    cart = get_or_create_cart(request)
    
    try:
        cart_item = cart.items.get(book=book, format=format)
        cart_item.delete()
        return True, f"Removed {book.title} ({format}) from your cart"
    except CartItem.DoesNotExist:
        return False, "Item not found in cart"


def update_cart_item_quantity(request, isbn, format, quantity):
    """
    Update quantity of item in cart
    """
    try:
        book = Books.objects.get(isbn=isbn)
    except Books.DoesNotExist:
        return False, "Book not found"
    
    cart = get_or_create_cart(request)
    
    try:
        cart_item = cart.items.get(book=book, format=format)
        if quantity <= 0:
            cart_item.delete()
            return True, f"Removed {book.title} ({format}) from your cart"
        else:
            cart_item.quantity = quantity
            cart_item.save()
            return True, f"Updated {book.title} ({format}) quantity to {quantity}"
    except CartItem.DoesNotExist:
        return False, "Item not found in cart"


def clear_cart(request):
    """
    Clear all items from cart
    """
    cart = get_or_create_cart(request)
    cart.clear()
    return True, "Cart cleared"


def migrate_session_to_db_cart(request):
    """
    Migrate old session-based cart to database cart
    This is for backwards compatibility during transition
    """
    session_bag = request.session.get('bag', {})
    if not session_bag:
        return
    
    cart = get_or_create_cart(request)
    
    for item_isbn, item_data in session_bag.items():
        try:
            book = Books.objects.get(isbn=item_isbn)
            
            if isinstance(item_data, int):
                # Old format: just quantity (assumes softcover)
                if book.price_softcover is not None:
                    cart_item, created = CartItem.objects.get_or_create(
                        cart=cart,
                        book=book,
                        format='softcover',
                        defaults={'quantity': item_data}
                    )
                    if not created:
                        cart_item.quantity += item_data
                        cart_item.save()
            else:
                # New format: {format: quantity}
                for format, quantity in item_data.items():
                    if format in ['softcover', 'hardcover', 'audiobook']:
                        # Check if price exists for this format
                        price = getattr(book, f'price_{format}', None)
                        if price is not None:
                            cart_item, created = CartItem.objects.get_or_create(
                                cart=cart,
                                book=book,
                                format=format,
                                defaults={'quantity': quantity}
                            )
                            if not created:
                                cart_item.quantity += quantity
                                cart_item.save()
        except Books.DoesNotExist:
            continue
    
    # Clear the session bag after migration
    if 'bag' in request.session:
        del request.session['bag']