from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from books.models import Books
from decimal import Decimal


class Cart(models.Model):
    """
    Shopping cart model that persists cart data in database
    instead of sessions for better user experience
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['user'], ['session_key']]

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        return f"Anonymous cart {self.session_key}"

    def get_total_cost(self):
        """Calculate total cost of all items in cart"""
        return sum(item.get_total_price() for item in self.items.all())

    def get_total_items(self):
        """Get total number of items in cart"""
        return sum(item.quantity for item in self.items.all())

    def clear(self):
        """Remove all items from cart"""
        self.items.all().delete()


class CartItem(models.Model):
    """
    Individual items in the shopping cart
    """
    FORMAT_CHOICES = [
        ('softcover', 'Softcover'),
        ('hardcover', 'Hardcover'),
        ('audiobook', 'Audiobook'),
    ]

    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['cart', 'book', 'format']]

    def __str__(self):
        return f"{self.quantity}x {self.book.title} ({self.format})"

    def get_price(self):
        """Get price for this book format"""
        if self.format == 'softcover':
            return self.book.price_softcover
        elif self.format == 'hardcover':
            return self.book.price_hardcover
        elif self.format == 'audiobook':
            return self.book.price_audiobook
        return None

    def get_total_price(self):
        """Calculate total price for this cart item"""
        price = self.get_price()
        if price is None:
            return Decimal('0.00')
        return price * self.quantity

    def is_valid(self):
        """Check if this cart item has a valid price"""
        return self.get_price() is not None

    def save(self, *args, **kwargs):
        """Validate price exists before saving"""
        if not self.is_valid():
            raise ValueError(f'Price not available for {self.format} format of {self.book.title}')
        super().save(*args, **kwargs)
