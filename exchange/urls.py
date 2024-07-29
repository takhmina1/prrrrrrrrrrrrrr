from django.urls import path
from .views import CurrencyListView, CurrencyConversionView

urlpatterns = [
    path('currencies/', CurrencyListView.as_view(), name='currency-list'),  # Список валют
    path('convert/', CurrencyConversionView.as_view(), name='currency-conversion'),  # Конвертация валют
    # path('update-rates/', UpdateCurrencyRatesView.as_view(), name='update-currency-rates'),  # Обновление курсов валют
]
