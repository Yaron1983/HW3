from django import forms
from .models import Author, Genre, Book


class BookSearchForm(forms.Form):
    author = forms.CharField(required=False, label='Author Name')
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        label="Genre",
        empty_label="All genres"
    )



