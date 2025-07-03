from django import forms
from .models import Book_Review_forms

class user_form(forms.ModelForm):
    class Meta:
        model=Book_Review_forms
        fields=['book_name','book_photo','book_url','book_review']
