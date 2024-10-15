from django.db import models
from django.contrib.auth.models import User

# A text choices category model for product category

class Category(models.TextChoices):
    ELECTRONICS = 'Electronics'
    BEAUTY = 'Beauty'
    TOOLS = 'Tools'
    CLOTHES = 'Clothes'
    CONSUMABLES = 'Consumables'
    AUTOMOTIVE = 'Automotive'

class Product(models.Model):
    name = models.CharField(max_length=200,default="",blank=False)
    description = models.TextField(max_length=1000,default="",blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    category = models.CharField(max_length=50,choices=Category.choices)
    stock_quantity = models.IntegerField(default="",blank=False)
    image_url = models.URLField(max_length=200,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    ratings = models.DecimalField(max_digits=3,decimal_places=2,default=0,blank=True)
    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

