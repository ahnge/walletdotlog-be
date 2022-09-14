from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomRegisterSerializer(RegisterSerializer):
    full_name = serializers.CharField(max_length=150)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        print(self.data)
        user.full_name = self.data.get('full_name')
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['profile_img'] = user.image_url
        token['full_name'] = user.full_name
        token['email'] = user.email
        # ...

        return token
