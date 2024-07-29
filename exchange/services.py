from decimal import Decimal
from .models import Currency

class CurrencyConverter:
    @staticmethod
    def convert(amount, from_currency, to_currency):
        """
        Конвертирует сумму из одной валюты в другую.
        
        Args:
            amount (Decimal): Сумма для конвертации.
            from_currency (str): Символ исходной валюты.
            to_currency (str): Символ целевой валюты.
        
        Returns:
            Decimal: Конвертированная сумма.
        """
        from_currency_obj = Currency.objects.get(symbol=from_currency)
        to_currency_obj = Currency.objects.get(symbol=to_currency)
        
        # Конвертация в USD, затем в целевую валюту
        amount_in_usd = amount / from_currency_obj.rate_to_usd
        converted_amount = amount_in_usd * to_currency_obj.rate_to_usd
        
        return converted_amount
