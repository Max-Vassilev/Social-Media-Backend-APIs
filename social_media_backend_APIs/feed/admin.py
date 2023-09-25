from django.contrib import admin

from social_media_backend_APIs.feed.models import Post


@admin.register(Post)
class UserModelAdmin(admin.ModelAdmin):
    pass
