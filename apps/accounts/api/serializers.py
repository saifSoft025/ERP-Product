from rest_framework import serializers

from apps.accounts.models import User
from apps.accounts.services.auth_service import AuthService


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
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

    def create(self, validated_data):
        return AuthService.register(validated_data)