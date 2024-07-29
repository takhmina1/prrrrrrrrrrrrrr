from django.urls import path
from .views import CurrencyPairListView, CurrencyPairDetailView, CurrencyConversionView

urlpatterns = [
    path('api/currency-pairs/', CurrencyPairListView.as_view(), name='currency_pairs_list'),
    path('api/currency-pairs/<int:pk>/', CurrencyPairDetailView.as_view(), name='currency_pair_detail'),
    path('api/currency-conversion/', CurrencyConversionView.as_view(), name='currency_conversion'),
]
