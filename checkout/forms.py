from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number', 'street_address1', 
                  'street_address2', 'town_or_city', 'postcode', 'county', 'country']
        
    def __init__(self, *args, **kwargs):
        '''
        Add placeholders and classes, remove auto-generated labels
        and set autofocus on first field
        '''
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality'
        }
        
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Handle all fields normally now that country is a regular CharField
        for field_name in self.fields:
            field = self.fields[field_name]
            if field_name in placeholders:
                if field.required:
                    placeholder = f'{placeholders[field_name]} *'
                else:
                    placeholder = placeholders[field_name]
                field.widget.attrs['placeholder'] = placeholder
            field.widget.attrs['class'] = 'stripe-style-input form-control'
            field.label = False
        