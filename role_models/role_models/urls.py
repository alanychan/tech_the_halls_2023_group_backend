from django.contrib import admin
from django.urls import path, include

admin.site.index_title = 'Tech The Halls'
admin.site.site_header = 'Tech The Halls'
admin.site.site_title = 'Tech The Halls Group Project.'
admin.site.site_url = '/users'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    # path('', include('profiles.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('hero.urls')),
]
