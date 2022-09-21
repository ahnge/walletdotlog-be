from django.urls import path
from . import views

app_name = 'wallet_api'


urlpatterns = [
    path('list-create/', views.WalletListCreate.as_view(),
         name='wallet_list_create'),
    path('<int:pk>/log/list-create/',
         views.LogListCreate.as_view(), name='log_list_create'),
    path('<int:pk>/log/list/latest/',
         views.LatestLogsList.as_view(), name='latest_log_list'),
]
