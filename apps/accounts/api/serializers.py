from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.accounts.services.auth_service import AuthService
from .validators import PasswordValidator

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User

        fields = (
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
        )

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "Email already exists."
            )

        return value
    #  validate_username and validate_password methods are used to validate the username and password fields respectively.

    def validate_username(self, value):

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                "Username already exists."
            )

        return value

    def validate_password(self, value):

        PasswordValidator.validate(value)

        return value

    def create(self, validated_data):

        return AuthService.register(validated_data)