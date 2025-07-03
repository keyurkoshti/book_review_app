from django.db import models

# Create your models here.
class Book_Review_forms(models.Model):
    book_name=models.CharField(max_length=50)
    book_photo=models.ImageField(upload_to='book_photos/')
    book_url=models.URLField()
    book_review=models.CharField(max_length=500)

    def __str__(self):
        return self.book_name

    

