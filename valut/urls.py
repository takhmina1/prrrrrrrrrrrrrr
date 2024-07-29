from django.urls import path
from .views import CurrencyExchangeView, CurrencyListView, PaymentDetailsView, PaymentHistoryView

urlpatterns = [
    path('exchange/', CurrencyExchangeView.as_view(), name='currency-exchange'),
    path('currencies/', CurrencyListView.as_view(), name='currency-list'),
    path('payment-details/', PaymentDetailsView.as_view(), name='payment-details'),
    path('payment-history/', PaymentHistoryView.as_view(), name='payment-history'),
]
