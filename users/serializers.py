from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
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
        token['full_name'] = user.full_name
        token['email'] = user.email
        if user.image.url == 'https://walletdotlog.s3.ap-southeast-1.amazonaws.com/user_profile/default_profile.jpg?AWSAccessKeyId=AKIAVEHZQZECOLLEECO3&Signature=6oZiI96AA3oUMsgky%2FCtGGpygUo%3D&Expires=1665414368':
            if user.social_image:
                token['profile_img'] = user.social_image
            else:
                token['profile_img'] = f"{user.image.url}"
        else:
            token['profile_img'] = f"{user.image.url}"

        # ...

        return token


class CustomUserDetailSerializer(UserDetailsSerializer):
    full_name = serializers.CharField(max_length=150)
    image = serializers.ImageField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('full_name', 'image')
