from django.contrib.auth import login, logout
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from social_media_backend_APIs.users.models import SocialMediaUser
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaUser
        fields = ["username", "email", "password"]


# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SocialMediaUser
#         fields = ["email", "password"]


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


class LoginUserViewAPI(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = get_object_or_404(SocialMediaUser, email=email)

        # Check if the password is correct:
        if not user.check_password(password):
            return Response({"message": "Wrong email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            login(request, user)
            return Response({"message": "Login successful."})


class LogoutUserViewAPI(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "User is not logged in."}, status=status.HTTP_401_UNAUTHORIZED)
