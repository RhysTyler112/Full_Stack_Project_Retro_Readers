import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings 
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from books.models import Books
from profiles.models import UserProfile

from django_countries.fields import CountryField


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, 
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    email_sent = models.BooleanField(default=False)
    webhook_received = models.BooleanField(default=False)
    def _generate_order_number(self):
        '''
        Generate a random, unique order number using UUID
        '''
        return uuid.uuid4().hex.upper()
    
    
    def update_total(self):
        '''
        Update grand total each time a line item is added,
        accounting for delivery costs
        '''
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
            
    
    def save(self, *args, **kwargs):
        '''
        Override the original save method to set the order number 
        if it hasn't been set already
        '''
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    book = models.ForeignKey(Books, null=False, blank=False, on_delete=models.CASCADE)
    format = models.CharField(max_length=9, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    
    def save(self, *args, **kwargs):
        '''
        Override the original save method to set the lineitem_total
        based on the format and quantity
        '''
        price = None
        
        if self.format == 'softcover':
            price = self.book.price_softcover
        elif self.format == 'hardcover':
            price = self.book.price_hardcover
        elif self.format == 'audiobook':
            price = self.book.price_audiobook
        
        # Handle null prices
        if price is None:
            raise ValueError(f'Price not set for {self.format} format of book: {self.book.title}')
        
        self.lineitem_total = price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.book.sku} on order {self.order.order_number}'
    
@receiver(pre_save, sender=Order)
def update_grand_total(sender, instance, **kwargs):
    instance.grand_total = instance.order_total + instance.delivery_cost

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()