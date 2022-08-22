from rest_framework import serializers

from shops.models import Brand, Product, Item, Order


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductReadOnlySerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'        
        

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = '__all__'
        
        
class ItemReadOnlySerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Item
        fields = '__all__'              


class OrderReadOnlySerializer(serializers.ModelSerializer):
    items = ItemReadOnlySerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        
        
class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'