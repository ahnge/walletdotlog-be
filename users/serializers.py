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
        user.full_name = self.data.get("full_name")
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["full_name"] = user.full_name
        token["email"] = user.email
        if user.image.file.name == "profile_pictures/default_profile.jpeg":
            if user.social_image:
                token["profile_img"] = user.social_image
            else:
                token["profile_img"] = f"{user.image.url}"
        else:
            token["profile_img"] = f"{user.image.url}"

        # ...

        return token


class CustomUserDetailSerializer(UserDetailsSerializer):
    full_name = serializers.CharField(max_length=150)
    image = serializers.ImageField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ("full_name", "image")
