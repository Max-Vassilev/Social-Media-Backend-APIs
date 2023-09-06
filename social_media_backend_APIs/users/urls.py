from django.urls import path
from social_media_backend_APIs.users.views import *

urlpatterns = [
    path('register/', RegisterUserViewAPI.as_view(), name='resister API')
]