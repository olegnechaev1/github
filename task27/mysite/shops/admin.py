from django.contrib import admin
from .models import Brand, Product, Cart, Order, Item


class BrandModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    ) 
    
    
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'name',
        'description',
        'photo',
    )
    
    
class CartModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )
    
    
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )
    readonly_fields = ('total_price',)

    def total_price(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.price
        return total
     
    
class ItemModelAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'price',
        'available',
    )                 


admin.site.register(Brand, BrandModelAdmin)    
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Cart, CartModelAdmin)
admin.site.register(Order, OrderModelAdmin)
admin.site.register(Item, ItemModelAdmin)
