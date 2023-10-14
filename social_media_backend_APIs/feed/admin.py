from django.contrib import admin

from social_media_backend_APIs.feed.models import Post, Like


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeModelAdmin(admin.ModelAdmin):
    pass
