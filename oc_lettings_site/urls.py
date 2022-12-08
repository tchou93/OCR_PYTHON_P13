from django.contrib import admin
from django.urls import path, include

app_name = 'main'


def trigger_error():
    return 1 / 0


urlpatterns = [
    path('', include('apps.lettings.urls')),
    path('', include('apps.profiles.urls')),
    path('', include('apps.main.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
