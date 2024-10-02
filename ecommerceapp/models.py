from django.db import models
from django.contrib.auth.models import User

# Create your models here.

state_choices = (
    ("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")
    )

category = (
    ("Laptop", "Laptop"),
    ("Mobile", "Mobile"),
    ("Top Wear", "Top Wear"),
    ("Bottom Wear", "Bottom Wear"),
    )

status = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=state_choices, max_length=100)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=category, max_length=50, null=True)
    image = models.ImageField(upload_to='uploadimages', null=True)
    rating = models.FloatField(default=1)
    off_percentage = models.IntegerField()
    original_price = models.IntegerField()
    discounted_price = models.IntegerField()


class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class OrderPlaced(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(choices=status, max_length=100, default="Pending")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
