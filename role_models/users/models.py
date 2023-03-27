from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models in here.

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


# class Question(models.Model):
#     question = models.CharField(max_length=500)
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['question']

#     def __str__(self):
#         return self.category_name