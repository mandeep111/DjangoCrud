from django import forms
from .models import Book
class CreateBook(forms.ModelForm):
    class meta:
        model = Book
        fields = '__all__'