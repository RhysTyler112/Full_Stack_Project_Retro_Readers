from django.contrib import admin
from django import forms
from .models import Books, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        isbn = cleaned_data.get("isbn")

        if isbn:
            book = Books(isbn=isbn)
            book.fetch_book_details()

            # Only update fields if they are empty
            if not cleaned_data.get("title"):
                cleaned_data["title"] = book.title
            if not cleaned_data.get("author"):
                cleaned_data["author"] = book.author
            if not cleaned_data.get("realised_date"):
                cleaned_data["realised_date"] = book.realised_date
            if not cleaned_data.get("image_url"):
                cleaned_data["image_url"] = book.image_url
        return cleaned_data

@admin.register(Books)
class BooksAdmins(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "author", "isbn", "realised_date", "category")
    search_fields = ("title", "author", "isbn")
    ordering = ("category",)

admin.site.register(Category)