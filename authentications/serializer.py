from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response

from authentications.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "email", "phone_number", "password",
            "is_vendor", "created_at", "updated_at"
        ]

    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            phone_number=validate_data['phone_number'],
        )
        user.set_password(validate_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email", "password"]


class ForgetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email"]
