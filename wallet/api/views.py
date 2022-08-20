from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import WalletSerializer, LogSerializer
from wallet.models import Wallet


class WalletList(ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return user.wallet_set.all()
