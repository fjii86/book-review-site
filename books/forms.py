from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']  # Viktigt!
        widgets = {
            'rating': forms.NumberInput(attrs={
            'min': 1, 
            'max': 5, 
            'class': 'form-control w-auto',
            'style': 'display: inline-block; width: 80px;',
        }),
        'content': forms.Textarea(attrs={
        'rows': 3, 
        'class': 'form-control'
        }),
        } 
        labels = {
            'rating': 'Rating (1–5)',
            'content': 'Your Review',
        }