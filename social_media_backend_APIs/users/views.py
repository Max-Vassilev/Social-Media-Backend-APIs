from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from social_media_backend_APIs.users.models import SocialMediaUser
from rest_framework.authtoken.models import Token


# Create your views here.

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaUser
        fields = ["username", "email", "password"]


class RegisterUserViewAPI(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        # Check if the data is right for user registration:
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)

            # Password hashing:
            user.set_password(request.data["password"])
            user.save()

            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
