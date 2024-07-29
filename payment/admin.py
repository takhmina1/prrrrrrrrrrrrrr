from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('email', 'sender_name', 'sberbank_card', 'tether_wallet', 'paypal_payment_id', 'amount', 'currency', 'description', 'created_at', 'status')
    search_fields = ('email', 'sender_name', 'sberbank_card', 'tether_wallet', 'paypal_payment_id')
    list_filter = ('currency', 'status', 'created_at')
    ordering = ('-created_at',)
