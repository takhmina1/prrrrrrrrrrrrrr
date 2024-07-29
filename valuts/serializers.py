from rest_framework import serializers
from .models import Currency, CurrencyPair

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'code']

class CurrencyPairSerializer(serializers.ModelSerializer):
    source_currency = CurrencySerializer()
    target_currency = CurrencySerializer()

    class Meta:
        model = CurrencyPair
        fields = ['id', 'source_currency', 'target_currency', 'logo', 'buy', 'sell', 'is_active']

class CurrencyConversionRequestSerializer(serializers.Serializer):
    source_currency = serializers.CharField(max_length=10)
    target_currency = serializers.CharField(max_length=10)
    amount = serializers.DecimalField(max_digits=15, decimal_places=2)
