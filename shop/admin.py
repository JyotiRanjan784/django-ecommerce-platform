from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Order,OrderUpdate
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(OrderUpdate)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'name', 'get_amount_display']

    def get_amount_display(self, obj):
        return f"₹{obj.amount:,}/-"

    get_amount_display.short_description = "Amount"

admin.site.register(Order, OrdersAdmin)