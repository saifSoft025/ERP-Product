from apps.accounts.models import User


class AuthService:

    @staticmethod
    def register(validated_data):
        return User.objects.create_user(**validated_data)