from rest_framework import serializers
from shop.models import Product, Order, OrderUpdate
from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'category',
            'subcategory',
            'price',
            'desc',
            'pub_date',
            'image',
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'order_id',
            'items_json',
            'amount',
            'created_at',
            'name',
            'email',
            'address',
            'city',
            'state',
            'zip_code',
            'phone',
            'payment_status',
            'paid',
        ]
        read_only_fields = [
            'order_id',
            'created_at',
            'payment_status',
            'paid',
        ]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Order amount must be greater than zero."
            )

        return value

    def validate_items_json(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Order items cannot be empty."
            )

        return value

    def create(self, validated_data):
        user = self.context['request'].user

        order = Order.objects.create(
            user=user,
            **validated_data
        )

        OrderUpdate.objects.create(
            order_id=order.order_id,
            update_desc='The order has been placed successfully'
        )

        return order


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUpdate
        fields = [
            'update_id',
            'order_id',
            'update_desc',
            'timestamp',
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user