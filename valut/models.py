from django.db import models

class Currency(models.Model):
    TYPE_CHOICES = [
        ('fiat', 'Фиатная валюта'),  # Фиатные валюты (например, USD, EUR)
        ('crypto', 'Криптовалюта'),  # Криптовалюты (например, BTC, ETH)
        ('eps', 'Электронная платёжная система'),  # Электронные платёжные системы (например, PayPal)
        ('other', 'Другое'),  # Другие типы валют
    ]

    name = models.CharField(max_length=100)  # Название валюты
    code = models.CharField(max_length=10, unique=True)  # Код валюты (уникальный)
    symbol = models.CharField(max_length=10, blank=True)  # Символ валюты (например, "$")
    icon = models.ImageField(upload_to='currency_icons/', null=True, blank=True)  # Иконка валюты
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True, null=True)  # Тип валюты (из списка TYPE_CHOICES)
    base_commission = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Базовая комиссия в процентах
    rate = models.DecimalField(max_digits=10, decimal_places=6, default=1.0) 


    def __str__(self):
        return self.name  # Возвращает название валюты при преобразовании объекта в строку

    class Meta:
        verbose_name = 'Валюта'  # Название модели в единственном числе
        verbose_name_plural = 'Валюты'  # Название модели во множественном числе

class PaymentDetails(models.Model):
    email = models.EmailField(verbose_name='E-mail')  # E-mail отправителя
    full_name = models.CharField(max_length=255, verbose_name='ФИО отправителя')  # ФИО отправителя
    sberbank_card_number = models.CharField(max_length=18, verbose_name='Карта Сбербанка')  # Номер карты Сбербанка
    tether_wallet = models.CharField(max_length=255, verbose_name='Кошелёк Tether (TRC20)')  # Кошелёк Tether (TRC20)
    agree_to_exchange_rules = models.BooleanField(verbose_name='Я согласен с правилами обмена и политикой AML')  # Согласие с правилами обмена и политикой AML

    def __str__(self):
        return f'Payment Details for {self.full_name}'  # Возвращает строку с информацией о платёжных реквизитах

    class Meta:
        verbose_name = 'Реквизиты оплаты'  # Название модели в единственном числе
        verbose_name_plural = 'Реквизиты оплаты'  # Название модели во множественном числе

class PaymentHistory(models.Model):
    payment_details = models.ForeignKey(PaymentDetails, related_name='payments', on_delete=models.CASCADE)  # Связь с реквизитами оплаты
    payment_date = models.DateTimeField(auto_now_add=True)  # Дата и время платежа

    def __str__(self):
        return f'Payment #{self.id} for {self.payment_details.full_name}'  # Возвращает строку с номером платежа и ФИО отправителя

    class Meta:
        verbose_name = 'История платежей'  # Название модели в единственном числе
        verbose_name_plural = 'История платежей'  # Название модели во множественном числе
