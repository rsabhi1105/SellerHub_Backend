from django.contrib import admin

from payment_api.models import Order


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_product", "order_amount", "order_payment_id",
        "isPaid", "order_date", "updated_at",
    ]
