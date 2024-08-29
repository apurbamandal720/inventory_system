from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    popularity_score = models.FloatField(default=0.0)
    sales_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Sale(models.Model):
    product = models.ForeignKey(Product, related_name='sales', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=Sale)
def update_popularity_score(sender, instance, **kwargs):
    product = instance.product
    product.sales_count = product.sales_count + instance.quantity
    product.popularity_score = calculate_popularity(product.sales_count)
    product.inventory_count = product.inventory_count - instance.quantity
    product.save()

def calculate_popularity(sales_count):
    return sales_count * 0.7