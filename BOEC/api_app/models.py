from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.IntegerField( null=True)
    quantity = models.IntegerField( null=True)
    regular_price = models.IntegerField( null=True)
    sale_price = models.IntegerField( null=True),
    on_sale = models.IntegerField( null=True),
    images = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    images = models.CharField(max_length=255, null=True)
