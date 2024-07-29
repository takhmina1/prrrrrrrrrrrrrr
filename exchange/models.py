from django.db import models

class Currency(models.Model):
    CATEGORY_CHOICES = [
        ('Фиат', 'Фиат'),  # Фиатные валюты (например, USD, EUR)
        ('Криптовалюта', 'Криптовалюта'),  # Криптовалюты (например, Bitcoin, Ethereum)
    ]

    # Название валюты
    name = models.CharField(max_length=100)
    # Символ валюты (например, USD, BTC)
    symbol = models.CharField(max_length=10, unique=True)
    # URL логотипа валюты
    logo = models.URLField()
    # Курс валют (по отношению к USD или другой базовой валюте)
    rate_to_usd = models.DecimalField(max_digits=15, decimal_places=6)
    # Категория валюты (Фиат или Криптовалюта)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # Статус активности валюты
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # Возвращает строковое представление валюты
        return f"{self.name} ({self.symbol})"




"""
from exchange_app.models import Currency

# Пример добавления фиатной валюты
fiat_currency = Currency(
    name="Доллар США",
    symbol="USD",
    logo="https://example.com/usd_logo.png",
    rate_to_usd=1.0,
    category="Фиат",
    is_active=True
)
fiat_currency.save()

# Пример добавления криптовалюты
crypto_currency = Currency(
    name="Биткойн",
    symbol="BTC",
    logo="https://example.com/btc_logo.png",
    rate_to_usd=30000.0,
    category="Криптовалюта",
    is_active=True
)
crypto_currency.save()

"""
