from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CurrencyPair
from .serializers import CurrencyPairSerializer, CurrencyConversionRequestSerializer

class CurrencyPairListView(APIView):
    def get(self, request):
        currency_pairs = CurrencyPair.objects.filter(is_active=True)
        serializer = CurrencyPairSerializer(currency_pairs, many=True)
        serializer = CurrencyPairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        else:
            except as e:
            return raise Response({'erors': str(e)})
            # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        return Response({'data': serializer.data, status=status.HTTP_200_OK})
    


    def post(self, request):
        serializer = CurrencyPairSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'currency': serializer.data, status=status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrencyPairDetailView(APIView):
    def get_object(self, pk):
        try:
            return CurrencyPair.objects.get(pk=pk)
        except CurrencyPair.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        currency_pair = self.get_object(pk)
        serializer = CurrencyPairSerializer(currency_pair)
        return Response(serializer.data)

    def put(self, request, pk):
        currency_pair = self.get_object(pk)
        serializer = CurrencyPairSerializer(currency_pair, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        currency_pair = self.get_object(pk)
        currency_pair.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CurrencyConversionView(APIView):
    def post(self, request):
        serializer = CurrencyConversionRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            source_currency_code = data['source_currency']
            target_currency_code = data['target_currency']
            amount = data['amount']

            try:
                source_currency = Currency.objects.get(code=source_currency_code)
                target_currency = Currency.objects.get(code=target_currency_code)
                currency_pair = CurrencyPair.objects.get(
                    source_currency=source_currency,
                    target_currency=target_currency,
                    is_active=True
                )

                converted_amount = amount * currency_pair.buy  # Предположим, что buy - это курс покупки
                response_data = {
                    'source_currency': source_currency_code,
                    'target_currency': target_currency_code,
                    'amount': amount,
                    'converted_amount': converted_amount,
                    'exchange_rate': currency_pair.buy  # Возвращаем текущий курс
                }

                return Response(response_data, status=status.HTTP_200_OK)

            except Currency.DoesNotExist:
                return Response({'error': 'One of the currencies does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            except CurrencyPair.DoesNotExist:
                return Response({'error': 'Currency pair does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
