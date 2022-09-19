from rest_framework import serializers
from wallet.models import Wallet, Log


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['log_type', 'amount', 'description']
