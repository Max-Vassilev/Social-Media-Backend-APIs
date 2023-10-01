from django.urls import path
from social_media_backend_APIs.feed.views import *

urlpatterns = [

    path("all-posts/", AllPostsViewAPI.as_view(), name="all posts API"),
    path("create-post/", CreatePostViewAPI.as_view(), name="create post API"),
    path("delete-post/<int:pk>/", DeletePostViewAPI.as_view(), name="delete post API"),
    #
    # path("like-post/<int:pk>/", LikePostViewAPI.as_view(), name="like post"),
    # path("unlike-post/<int:pk>/", UnlikePostViewAPI.as_view(), name="unlike post"),

]
