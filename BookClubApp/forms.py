from django import forms
from .models import Club, Book

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'summary', 'club']
