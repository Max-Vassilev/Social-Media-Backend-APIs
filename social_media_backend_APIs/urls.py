from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('social_media_backend_APIs.users.urls')),
    path('feed/', include('social_media_backend_APIs.feed.urls')),
    path('main/', include('social_media_backend_APIs.main.urls')),
]
