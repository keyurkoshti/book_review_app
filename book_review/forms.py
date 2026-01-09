from django import forms 
from .models import Book_Review_forms

class user_form(forms.ModelForm):
    class Meta:
        model=Book_Review_forms
        fields=['user','book','book_photo','book_url','book_review']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].empty_label = "Select Book..."