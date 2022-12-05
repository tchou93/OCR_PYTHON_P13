from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('apps.lettings.urls')),
    path('', include('apps.profiles.urls')),
    path('admin/', admin.site.urls),
]
