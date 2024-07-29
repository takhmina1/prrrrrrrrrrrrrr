from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from decimal import Decimal
from .models import Currency
from .serializers import CurrencySerializer
from .services import CurrencyConverter

class CurrencyListView(APIView):
    def get(self, request):
        """
        Получает список всех валют.
        """
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Создает новую валюту.
        """
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrencyConversionView(APIView):
    def post(self, request):
        """
        Обрабатывает запрос на конвертацию валюты.
        """
        amount = request.data.get('amount')
        from_currency = request.data.get('from_currency')
        to_currency = request.data.get('to_currency')

        if not all([amount, from_currency, to_currency]):
            return Response({"error": "Недостаточно данных для конвертации."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            converted_amount = CurrencyConverter.convert(Decimal(amount), from_currency, to_currency)
            return Response({"converted_amount": converted_amount}, status=status.HTTP_200_OK)
        except Currency.DoesNotExist:
            return Response({"error": "Одна или обе валюты не найдены."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class UpdateCurrencyRatesView(APIView):
#     def post(self, request):
#         """
#         Обновляет курсы валют из внешнего API.
#         """
#         try:
#             rates = ExternalAPI.fetch_currency_rates()
#             for symbol, rate in rates.items():
#                 # Обновляем или создаем новую валюту в базе данных
#                 currency, created = Currency.objects.update_or_create(
#                     symbol=symbol,
#                     defaults={'rate_to_usd': rate}
#                 )
#             return Response({"message": "Курсы валют обновлены."}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
