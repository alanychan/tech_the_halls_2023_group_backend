from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class CustomUser(AbstractUser):

    categories = models.ManyToManyField(Category, related_name="user_categories")

    def __str__(self):
        return self.username


# class Question(models.Model):
#     question = models.CharField(max_length=500)
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['question']

#     def __str__(self):
#         return self.category_name