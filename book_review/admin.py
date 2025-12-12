from django.contrib import admin
from .models import Book_Review_forms
# Register your models here.


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_url', 'book_review')  # columns in list view
    search_fields = ('book_name',)  # search bar by book_name
    list_filter = ('book_name',)    # filter by book_name

admin.site.register(Book_Review_forms, BookReviewAdmin)