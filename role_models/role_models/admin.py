from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.users)

#register link
admin.site.site_url = "/users"
