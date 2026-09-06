from django.contrib import admin

from .models import Product, Contact, Order, OrderUpdate


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_name',
        'category',
        'subcategory',
        'get_price_display',
        'pub_date',
    ]

    search_fields = [
        'product_name',
        'category',
        'subcategory',
    ]

    list_filter = [
        'category',
        'subcategory',
        'pub_date',
    ]

    def get_price_display(self, obj):
        return f"₹{obj.price:,}/-"

    get_price_display.short_description = "Price"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'msg_id',
        'name',
        'email',
        'phone',
        'created_at',
    ]

    search_fields = [
        'name',
        'email',
        'phone',
    ]

    list_filter = [
        'created_at',
    ]


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'order_id',
        'name',
        'email',
        'get_amount_display',
        'payment_status',
        'paid',
        'created_at',
    ]

    search_fields = [
        'name',
        'email',
        'phone',
        'razorpay_order_id',
        'razorpay_payment_id',
    ]

    list_filter = [
        'payment_status',
        'paid',
        'created_at',
    ]

    def get_amount_display(self, obj):
        return f"₹{obj.amount:,}/-"

    get_amount_display.short_description = "Amount"


@admin.register(OrderUpdate)
class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = [
        'update_id',
        'order_id',
        'update_desc',
        'timestamp',
    ]

    search_fields = [
        'update_desc',
    ]

    list_filter = [
        'timestamp',
    ]