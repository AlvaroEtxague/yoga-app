from django.contrib import admin
from .models import StripeTransaction


@admin.register(StripeTransaction)
class StripeTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'txn_id', 'is_paid', 'created_at']
    search_fields = ['txn_id']
    list_filter = ('created_at',)
    list_per_page = 20
