from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics as api_views, serializers

from social_media_backend_APIs.feed.models import Post


class ViewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["content"]


class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = []


class AllPostsViewAPI(api_views.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ViewPostSerializer
    # Work if user is authenticated:
    permission_classes = [IsAuthenticated]


class CreatePostViewAPI(api_views.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CreatePostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the author as the currently authenticated user
        serializer.save(author=self.request.user)


class DeletePostViewAPI(api_views.UpdateAPIView):
    serializer_class = DeletePostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Post.objects.filter(pk=pk, author=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance:
            instance.delete()
            return Response({"message": "Post was hard deleted successfully."})

