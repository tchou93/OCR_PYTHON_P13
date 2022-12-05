from django.contrib import admin
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', include('apps.lettings.urls')),
    path('', include('apps.profiles.urls')),
    path('', include('apps.main.urls')),
    path('admin/', admin.site.urls),
]
