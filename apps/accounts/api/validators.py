from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class PasswordValidator:

#  func 
    @staticmethod
    def validate(password):

        try:
            validate_password(password)

        except ValidationError as e:
            raise ValidationError(e.messages)