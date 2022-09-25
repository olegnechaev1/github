from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Brand(models.Model):
    class Meta:
        ordering = ['-id']
    name = models.CharField(max_length=150, unique=True)
    
    def __str__(self):
        return str(self.name)


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,
                              related_name='brand'
                              )
    name = models.CharField(max_length=200, db_index=True)
    photo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f' {self.brand}, {self.name}, {self.description}, {self.photo}'
    

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, 
                                related_name='items'
                                )
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))]
                                )
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'Product: {self.product.name}. Price: {self.price}'
 

class Cart(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart for {self.user}'
    
    
class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='orders'
                             )
