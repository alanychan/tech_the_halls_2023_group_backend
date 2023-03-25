from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=200)
    # bio_pic = models.ImageField(upload_to='images/')
    bio_pic = models.URLField()
    bio_text = models.TextField()
    bio_url =models.URLField()
    featured = models.BooleanField()
    date_created = models.DateTimeField()