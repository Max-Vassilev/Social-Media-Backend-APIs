from django.urls import path
from social_media_backend_APIs.users.views import *

urlpatterns = [
    path('register/', RegisterUserViewAPI.as_view(), name='resister API'),
    path('login/', LoginUserViewAPI.as_view(), name='login API'),
    path('logout/', LogoutUserViewAPI.as_view(), name='logout API'),

]
