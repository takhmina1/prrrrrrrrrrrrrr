from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import perform_currency_exchange
from .serializers import CurrencySerializer, PaymentDetailsSerializer, PaymentHistorySerializer
from .models import Currency, PaymentDetails, PaymentHistory

class CurrencyExchangeView(APIView):
    def post(self, request):
        sender_currency_code = request.data.get('sender_currency')
        recipient_currency_code = request.data.get('recipient_currency')
        amount = request.data.get('amount')

        if not sender_currency_code or not recipient_currency_code or not amount:
            return Response(
                {"error": "sender_currency, recipient_currency, and amount are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            result = perform_currency_exchange(sender_currency_code, recipient_currency_code, amount)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(result, status=status.HTTP_200_OK)


class CurrencyListView(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        serializer.is_valid()
        serializer.save()
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

class PaymentDetailsView(APIView):
    def post(self, request):
        serializer = PaymentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentHistoryView(APIView):
    def get(self, request):
        payment_history = PaymentHistory.objects.all()
        serializer = PaymentHistorySerializer(payment_history, many=True)
        serializers.is_valid()
        serializser.save()
        return Response({'data': serializser.data })
