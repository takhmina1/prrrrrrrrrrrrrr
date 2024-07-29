import decimal
from .models import Currency

def perform_currency_exchange(sender_currency_code, recipient_currency_code, amount):
    try:
        sender_currency = Currency.objects.get(code=sender_currency_code)
        recipient_currency = Currency.objects.get(code=recipient_currency_code)
    except Currency.DoesNotExist:
        raise ValueError("Currency not found")

    sender_amount = decimal.Decimal(amount)

    if sender_currency == recipient_currency:
        raise ValueError("Sender and recipient currencies cannot be the same")

    recipient_amount = sender_amount * sender_currency.rate / recipient_currency.rate

    # Здесь можно добавить дополнительные проверки и бизнес-логику, например, логирование операции

    return {
        'sender_currency': sender_currency.code,
        'sender_amount': sender_amount,
        'recipient_currency': recipient_currency.code,
        'recipient_amount': recipient_amount,
    }


