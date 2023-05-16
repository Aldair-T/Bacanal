from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Products(models.Model):
    product_name = models.CharField(max_length=20, blank=False, null=False)
    brand_name = models.CharField(max_length=20, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    stock = models.IntegerField(default=0, blank=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.description


class Carrito(models.Model):
    paid = models.BooleanField(default=False)
    total = models.IntegerField(blank=False, null=False)
    create = models.DateField(default=date.today)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    detail = models.ManyToManyField (Products, through="Lista")

    def __str__(self):
        return self.user.username


class Lista(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def precio_total(self):
        return self.amount * self.product.price




    