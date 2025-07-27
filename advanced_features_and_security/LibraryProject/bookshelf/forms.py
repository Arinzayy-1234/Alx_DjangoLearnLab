
from django import forms
from . models import Book

class BookForm(forms.ModelForm):

    class Meta:

        model = Book
        fields = '__all__'

class ExampleForm(forms.Form):
    # This is a simple form with one text field.
    # You can add more fields if the check requires specific types,
    # but a basic CharField is usually sufficient for existence checks.
    your_name = forms.CharField(label='Your Name', max_length=100)
    your_email = forms.EmailField(label='Your Email')