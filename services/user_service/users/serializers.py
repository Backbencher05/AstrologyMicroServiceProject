from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()



"""
UserSerializer → to return user info (id, email, phone_number…).
👉 Example: when you hit /me/, you don’t want password field.
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone_number", "full_name", "gender", "language", "is_astrologer"]

"""
RegisterSerializer → to create a new user with validation.
👉 Example: when signup request comes, this ensures required fields are there, and password is hashed (not stored in plain text).
"""
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "phone_number", "full_name", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            phone_number=validated_data["phone_number"],
            full_name=validated_data.get("full_name", ""),
            password=validated_data["password"],
        )
        return user

"""
LoginResponseSerializer (optional helper) → structure the login response (access + refresh tokens).
"""
class LoginResponseSerializer(serializers.ModelSerializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["email", "access", "refresh"]
