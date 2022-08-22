from django.db import transaction
from rest_framework.decorators import action
from shops.models import Brand, Product, Order, Cart, Item
from shops.serializers import (
    ItemSerializer, ItemReadOnlySerializer, ProductSerializer,
    BrandSerializer, ProductReadOnlySerializer
)
from shops.serializers import OrderReadOnlySerializer, OrderSerializer
from rest_framework import viewsets, response, status
from .paginations import CustomPagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = CustomPagination
    
    #def get(self, request):
        #serializer = BrandSerializer(request.user)
        #return response.Response({"user": serializer.data})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductReadOnlySerializer
        return ProductSerializer

    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ItemReadOnlySerializer
        return ItemSerializer

    @transaction.atomic
    @action(
        detail=True,
        methods=['post'],
        url_path='add-cart'
    )
    def add_item_to_cart(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item = self.get_object()
        cart.items.add(item)
        return response.Response(status=status.HTTP_200_OK)
    
    @transaction.atomic
    @action(
        detail=False,
        methods=['get'],
        url_path='cart',
    )
    def cart(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = ItemReadOnlySerializer(cart.items.all(), many=True)
        return response.Response(serializer.data)
    
    @transaction.atomic
    @action(
        detail=False,
        methods=['delete'],
        url_path='cart',
    )
    def delete(self, request):
        cart = Cart.objects.get(user=request.user)
        cart.items.clear()    
        return response.Response(status=status.HTTP_204_NO_CONTENT)
    
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderReadOnlySerializer
        return OrderSerializer

    @transaction.atomic
    @action(
        detail=False,
        methods=['post'],
        url_path='create',
    )
    def create_order(self, request):
        cart = request.user.cart
        order = Order.objects.create(user=request.user)
        order.items.set(cart.items.all())
        cart.items.clear()
        serializer = self.get_serializer(order)
        return response.Response(serializer.data, 
                                 status=status.HTTP_201_CREATED
                                 )