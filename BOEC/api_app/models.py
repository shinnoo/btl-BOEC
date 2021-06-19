from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    price = models.IntegerField( null=True)
    description = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
    


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length=255, null=True)
