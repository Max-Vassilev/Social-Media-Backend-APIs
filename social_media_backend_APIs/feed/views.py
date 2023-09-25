from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics as api_views, serializers

from social_media_backend_APIs.feed.models import Post


class ViewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class AllPostsViewAPI(api_views.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ViewPostSerializer
    # Work if user is authenticated:
    permission_classes = [IsAuthenticated]
