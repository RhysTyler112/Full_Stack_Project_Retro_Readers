from django import forms
from .widgets import CustomClearableFileInput
from .models import Books, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance_original_isbn = self.instance.isbn  # Store original ISBN

    def clean(self):
        cleaned_data = super().clean()
        isbn = cleaned_data.get("isbn")

        # Fetch new data only if ISBN has changed or the book is new
        if isbn and isbn != self.instance_original_isbn:
            book = Books(isbn=isbn)
            book.fetch_book_details()

            # Only update fields if they are empty (preserves manual edits)
            cleaned_data["title"] = cleaned_data.get("title") or book.title
            cleaned_data["author"] = cleaned_data.get("author") or book.author
            cleaned_data["realised_date"] = cleaned_data.get("realised_date") or book.realised_date
            cleaned_data["image_url"] = cleaned_data.get("image_url") or book.image_url

        return cleaned_data
    
    
class  BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        
        self.fields['category'].choices = friendly_names
        for feild_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'