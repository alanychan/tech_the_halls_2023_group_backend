from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class CustomUser(AbstractUser):

    user_categories = models.ManyToManyField(Category, related_name="user_categories")

    def __str__(self):
        return self.username
