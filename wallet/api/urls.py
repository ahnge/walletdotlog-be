from django.urls import path
from . import views

app_name = 'wallet_api'


urlpatterns = [
    path('list-create/', views.WalletList.as_view(), name='wallet_list')
]
