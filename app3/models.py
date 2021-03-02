from django.db import models


# Create your models here.
class Book(models.Model):
    cover = models.ImageField(upload_to="book/cover/", null=True, blank=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='book/pdf')


    def __str__(self):
        return self.title
