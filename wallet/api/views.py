from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import WalletSerializer, LogSerializer
from wallet.models import Wallet, Log
from .utils import check_and_save


class WalletListCreate(ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    # queryset = Wallet.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LogListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req, pk):
        wallet = get_object_or_404(Wallet, pk=pk)
        if wallet.owner == self.request.user:
            logs = wallet.log_set.all()
            serializer = LogSerializer(logs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "You can't see logs you don't own."}, status=status.HTTP_403_FORBIDDEN)

    def post(self, req, pk):
        wallet = get_object_or_404(Wallet, pk=pk)
        serializer = LogSerializer(data=req.data)
        if wallet.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            check_and_save(wallet=wallet, serializer=serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "You can't edit other people's logs."}, status=status.HTTP_403_FORBIDDEN)


class LatestLogsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req, pk):
        wallet = get_object_or_404(Wallet, pk=pk)
        if wallet.owner == self.request.user:
            logs = wallet.log_set.all().order_by('-created_at')[:5]
            serializer = LogSerializer(logs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "You can't see logs you don't own."}, status=status.HTTP_403_FORBIDDEN)
