from django import forms
from .models import Rental

class BookRentForm(forms.BookRentForm):
    class Meta:
        model = Rental
        fields = ['name','whoo','who']
