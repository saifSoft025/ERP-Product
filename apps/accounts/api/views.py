from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer


class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "Account created successfully.",
                    "data": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )