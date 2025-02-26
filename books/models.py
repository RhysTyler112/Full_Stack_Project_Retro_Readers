import requests
from django.db import models

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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=13, null=True, blank=True, unique=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254, null=True, blank=True)
    realised_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

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
                self.title = data.get("title", self.title)
                self.author = ", ".join([author["name"] for author in data.get("authors", [])])
                self.realised_date = data.get("publish_date", None)  # Open Library provides a string
                self.description = data.get("description", {}).get("value", "")
                cover = data.get("cover", {}).get("large") or data.get("cover", {}).get("medium")
                self.image_url = cover if cover else self.image_url

    def save(self, *args, **kwargs):
        if not self.title or not self.author:  # Only fetch if details are missing
            self.fetch_book_details()
        super().save(*args, **kwargs)