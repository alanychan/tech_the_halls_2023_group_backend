from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Category)

#register link
admin.site.site_url = "/users"
admin.site.site_url = "/category"