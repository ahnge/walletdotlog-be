from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .serializers import WalletSerializer, LogSerializer
from wallet.models import Wallet
from .utils import check_and_save


class WalletListCreate(ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    # queryset = Wallet.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Wallet.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WalletDetail(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, req, pk):
        wallet = get_object_or_404(Wallet, pk=pk)
        serializer = WalletSerializer(data=req.data)
        if wallet.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            wallet.name = serializer.data["name"]
            wallet.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "You can't update wallet you don't own."}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, req, pk):
        wallet = get_object_or_404(Wallet, pk=pk)
        if wallet.owner == self.request.user:
            wallet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "You can't delete wallet you don't own."}, status=status.HTTP_403_FORBIDDEN)


class LogListCreate(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated]

    def get(self, req, pk):
        wallet = get_object_or_404(Wallet, pk=pk)
        if wallet.owner == self.request.user:
            search_params = req.GET.get("search")
            if search_params:
                logs = wallet.log_set.distinct().filter(description__icontains=search_params)
            else:
                logs = wallet.log_set.all().order_by("-created_at")
            results = self.paginate_queryset(logs, req, view=self)
            serializer = LogSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
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
