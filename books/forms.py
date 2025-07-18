from django import forms
from .models import Review, Book

class ReviewFormWithBook(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'rating', 'content']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control w-auto', 'style': 'width: 80px'}),
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'book': 'Book',
            'rating': 'Rating (1–5)',
            'content': 'Your Review',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control w-auto', 'style': 'width: 80px'}),
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'rating': 'Rating (1–5)',
            'content': 'Your Review',
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'cover', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'cover': 'Cover Image',
            'description': 'Description (optional)',
        }