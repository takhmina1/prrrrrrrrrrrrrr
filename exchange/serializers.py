from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', 'logo', 'rate_to_usd', 'category', 'is_active')

    def validate_symbol(self, value):
        """
        Проверяет, что символ валюты не пустой и уникальный.
        """
        if not value:
            raise serializers.ValidationError("Символ валюты не может быть пустым.")
        if Currency.objects.filter(symbol=value).exists():
            raise serializers.ValidationError("Символ валюты должен быть уникальным.")
        return value

    def validate_rate_to_usd(self, value):
        """
        Проверяет, что курс валюты положительный.
        """
        if value <= 0:
            raise serializers.ValidationError("Курс валюты должен быть положительным.")
        return value

    def validate(self, attrs):
        """
        Проверяет, что имя и символ валюты уникальны в комбинации.
        """
        if Currency.objects.filter(name=attrs.get('name'), symbol=attrs.get('symbol')).exists():
            raise serializers.ValidationError("Комбинация имени и символа валюты должна быть уникальной.")
        return attrs
