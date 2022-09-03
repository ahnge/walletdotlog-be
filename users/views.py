from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
import jwt
from .serializers import RegisterUserSerializer
from .models import CustomUser
from .utils import Utils

# Create your views here.


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, req):
        reg_serializer = RegisterUserSerializer(data=req.data)
        if reg_serializer.is_valid():
            reg_serializer.save()
            user_data = reg_serializer.data
            user = CustomUser.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user)

            current_site = get_current_site(req)
            relative_link = reverse('users:email_verify')
            abs_url = f"http://{current_site.domain}{relative_link}?token={token}"
            email_body = f"Hello {user.full_name}. Click the link below to verify your email \n {abs_url}"

            data = {'email_body': email_body,
                    'email_subject': 'Verify your email', 'to_email': user.email}
            Utils.send_email(data)

            return Response(reg_serializer.data, status=status.HTTP_201_CREATED)
        return Response(reg_serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class TokenBlackListView(APIView):
    permission_classes = [AllowAny]

    def post(self, req):
        try:
            refresh_token_string = req.data.get("refresh")
            token = RefreshToken(refresh_token_string)
            token.blacklist()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_202_ACCEPTED)
