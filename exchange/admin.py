from django.contrib import admin
from .models import Currency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'rate_to_usd', 'category', 'is_active')  # Поля, отображаемые в списке
    list_filter = ('category', 'is_active')  # Фильтры для боковой панели
    search_fields = ('name', 'symbol')  # Поля, по которым можно производить поиск
    ordering = ('name',)  # Поле для сортировки списка

    fieldsets = (
        (None, {
            'fields': ('name', 'symbol', 'logo', 'rate_to_usd', 'category', 'is_active')
        }),
    )

    # def get_queryset(self, request):
    #     """Изменяет набор данных для отображения в админке."""
    #     queryset = super().get_queryset(request)
    #     return queryset.filter(is_active=True)  # Отображает только активные валюты по умолчанию

