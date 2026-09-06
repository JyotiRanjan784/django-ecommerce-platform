from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shop.models import Product, Order, OrderUpdate

from .serializers import (
    ProductSerializer,
    OrderSerializer,
    OrderUpdateSerializer,
    RegisterSerializer
)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        return Response(
            {"detail": "Orders cannot be modified after placement."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {"detail": "Orders cannot be modified after placement."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def destroy(self, request, *args, **kwargs):
        return Response(
            {"detail": "Orders cannot be deleted."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class OrderUpdateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderUpdate.objects.filter(
            order_id__in=Order.objects.filter(
                user=self.request.user
            ).values_list('order_id', flat=True)
        )


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )