from django.db import models 
from django.contrib.auth.models import User  
from django.utils import timezone 

# Create your models here.
class Book_Review_forms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    book_name=models.CharField(max_length=50)
    book_photo=models.ImageField(upload_to='book_photos/')
    book_url=models.URLField()
    book_review=models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"{self.book_name} - {self.user}"


    

