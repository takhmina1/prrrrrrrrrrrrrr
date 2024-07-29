from rest_framework import serializers
from .models import FiatCurrency, Coin, Network, Transaction

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = (
            'name', 'deposit', 'receive', 'is_default',
            'confirmations_minimum', 'confirmations_maximum',
            'withdraw_decimals_minimum', 'regex_address', 'regex_tag',
            'has_tag', 'explorer', 'explorer_hash', 'explorer_address',
            'confirmation_minutes_range'
        )

    def validate_withdraw_decimals_minimum(self, value):
        if value < 0:
            raise serializers.ValidationError("Минимальное количество десятичных знаков для вывода не может быть отрицательным.")
        return value

class CoinSerializer(serializers.ModelSerializer):
    provider_info = serializers.SerializerMethodField()

    class Meta:
        model = Coin
        fields = (
            'coin', 'name', 'deposit_status_all', 'receive_status_all',
            'default_form_value', 'provider_info'
        )

    def validate_default_form_value(self, value):
        if value < 0:
            raise serializers.ValidationError("Значение по умолчанию не может быть отрицательным.")
        return value

    def get_provider_info(self, obj):
        networks = obj.networks.all()
        network_data = {}
        for network in networks:
            network_serializer = NetworkSerializer(network)
            network_data[network.coin.coin] = {
                'coin': network.coin.coin,
                'name': network.coin.name,
                'deposit_status_all': network.coin.deposit_status_all,
                'receive_status_all': network.coin.receive_status_all,
                'default_form_value': network.coin.default_form_value,
                'provider_info': {
                    'service': {
                        'network_list': {
                            network.name: network_serializer.data
                        }
                    }
                }
            }
        return network_data

class FiatCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FiatCurrency
        fields = '__all__'

    def validate_exchange_rate(self, value):
        if value <= 0:
            raise serializers.ValidationError("Курс обмена должен быть положительным числом.")
        return value

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Сумма транзакции должна быть положительным числом.")
        return value

    def validate(self, data):
        if data['source_currency'] == data['target_currency']:
            raise serializers.ValidationError("Исходная и целевая валюта не могут быть одинаковыми.")
        return data
