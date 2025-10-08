from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from books.models import Books

# Use the same country choices as in checkout
COUNTRY_CHOICES = [
    ('', 'Select Country'),
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    ('IE', 'Ireland'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('ES', 'Spain'),
    ('IT', 'Italy'),
    ('NL', 'Netherlands'),
    ('BE', 'Belgium'),
    ('AU', 'Australia'),
    ('CA', 'Canada'),
    ('NZ', 'New Zealand'),
    ('SE', 'Sweden'),
    ('NO', 'Norway'),
    ('DK', 'Denmark'),
    ('FI', 'Finland'),
]


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"