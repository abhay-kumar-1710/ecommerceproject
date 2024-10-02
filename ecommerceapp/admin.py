from django.contrib import admin
from ecommerceapp.models import Customer, Product, AddToCart, OrderPlaced

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'state', 'zipcode']
    ordering = ['id']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name', 'brand', 'category' , 'rating', 'original_price', 'discounted_price']
    ordering = ['id']

@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'quantity']
    ordering = ['id']

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer', 'product', 'quantity','status' ]
    ordering = ['id']