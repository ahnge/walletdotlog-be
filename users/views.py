from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer

# Create your views here.


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, req):
        reg_serializer = RegisterUserSerializer(data=req.data)
        if reg_serializer.is_valid():
            reg_serializer.save()
            return Response(reg_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reg_serializer._errors, status=status.HTTP_400_BAD_REQUEST)
