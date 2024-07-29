from django.contrib import admin
from .models import Currency, PaymentDetails, PaymentHistory

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type', 'rate')  # Поля для отображения в списке
    search_fields = ('name', 'code')  # Поля для поиска

class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'sberbank_card_number', 'tether_wallet', 'agree_to_exchange_rules')
    search_fields = ('email', 'full_name', 'sberbank_card_number', 'tether_wallet')

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('payment_details', 'payment_date')
    list_filter = ('payment_date',)
    search_fields = ('payment_details__full_name',)  # Поиск по связанному полю full_name в PaymentDetails

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)
