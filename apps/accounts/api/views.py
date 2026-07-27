from rest_framework import status
from rest_framework.views import APIView

from apps.common.utils.response import ApiResponse
from .serializers import RegisterSerializer


class RegisterAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.save()

        return ApiResponse.success(
            message="User registered successfully.",
            data={
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            status=status.HTTP_201_CREATED,
        )