from django.db import transaction

from apps.accounts.models import User


class AuthService:

    @staticmethod
    @transaction.atomic
    def register(validated_data):

        user = User.objects.create_user(
            **validated_data
        )

        return user