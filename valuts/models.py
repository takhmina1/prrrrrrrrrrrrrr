from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.code})"

class CurrencyPair(models.Model):
    CATEGORY_CHOICES = [
        ('Фиат', 'Фиат'),
        ('Криптовалюта', 'Криптовалюта'),
    ]

    source_currency = models.ForeignKey(Currency, related_name='source_currency_pairs', on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name='target_currency_pairs', on_delete=models.CASCADE)
    logo = models.URLField()
    buy = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    sell = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)
    source_decimal = models.IntegerField(default=1)
    target_decimal = models.IntegerField(default=1)
    source_regex = models.CharField(max_length=100)
    target_regex = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.source_currency} - {self.target_currency}"
