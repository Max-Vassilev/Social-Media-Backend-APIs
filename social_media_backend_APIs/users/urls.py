from django.urls import path
from social_media_backend_APIs.users.views import *

urlpatterns = [
    path('register/', RegisterUserViewAPI.as_view(), name='resister API'),
    path('login/', LoginUserViewAPI.as_view(), name='login API'),
    path('logout/', LogoutUserViewAPI.as_view(), name='logout API'),

    path('data/', DataUserViewAPI.as_view(), name='user data API'),

    path('delete/', DeleteUserViewAPI.as_view(), name='user delete API'),
    path('edit/', EditUserViewAPI.as_view(), name='user edit API'),

]
