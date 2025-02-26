from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['isbn', 'category']

    def clean(self):
        cleaned_data = super().clean()
        isbn = cleaned_data.get("isbn")

        if isbn:
            book = Books(isbn=isbn)
            book.fetch_book_details()
            cleaned_data["title"] = book.title
            cleaned_data["author"] = book.author
            cleaned_data["realised_date"] = book.realised_date
            cleaned_data["description"] = book.description
            cleaned_data["image_url"] = book.image_url

        return cleaned_data