from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('users/', include('users.urls')),
    path('', include('profiles.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('hero.urls')),
]
