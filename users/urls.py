from django.urls import path
from .views import RegisterUser, VerifyEmail

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register_user"),
    path('email-verify/', VerifyEmail.as_view(), name="email_verify"),
]
