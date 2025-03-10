import requests
from django.db import models
from datetime import datetime

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
class Books(models.Model):
    class Meta:
        verbose_name_plural = 'Books'
    
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=13, null=True, blank=True, unique=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    realised_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    price_softcover = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_hardcover = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price_audiobook = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

    def fetch_book_details(self):
        """
        Fetches book details from Open Library API using ISBN
        """
        if not self.isbn:
            return

        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{self.isbn}&format=json&jscmd=data"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get(f"ISBN:{self.isbn}", {})

            if data:
                if not self.title:
                    self.title = data.get("title", "Unknown Title")
                if not self.author:
                    self.author = ", ".join([author["name"] for author in data.get("authors", [])]) if data.get("authors") else "Unknown Author"
                raw_publish_date = data.get("publish_date", None)
                
                # Convert publish_date to YYYY-MM-DD format if possible
                if raw_publish_date and not self.realised_date:
                    try:
                        parsed_date = datetime.strptime(raw_publish_date, "%B %d, %Y")  # Example: "October 1, 1988"
                        self.realised_date = parsed_date.date()
                    except ValueError:
                        try:
                            parsed_date = datetime.strptime(raw_publish_date, "%Y")  # Example: "1988"
                            self.realised_date = parsed_date.date()
                        except ValueError:
                            self.realised_date = None  # If parsing fails, set to None
                
                cover = data.get("cover", {}).get("large") or data.get("cover", {}).get("medium")
                if not self.image_url:
                    self.image_url = cover if cover else self.image_url

    def save(self, *args, **kwargs):
        if not self.title or not self.author or not self.realised_date or not self.image_url:  # Only fetch if details are missing
            self.fetch_book_details()
        super().save(*args, **kwargs)
    
    def get_lowest_price(self):
        prices = [self.price_softcover, self.price_hardcover, self.price_audiobook]
        prices = [price for price in prices if price is not None]
        if prices:
            return min(prices)
        return None
    