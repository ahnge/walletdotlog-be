from rest_framework import serializers
from wallet.models import Wallet, Log


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['name', 'amount', 'id']


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['log_type', 'amount', 'description', 'id', 'created_at']

    # def to_representation(self, instance):
    #     """Convert `created_at` to human readable."""
    #     ret = super().to_representation(instance)
    #     ret['created_at'] = ret['created_at']
    #     return ret
