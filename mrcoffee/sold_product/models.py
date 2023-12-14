from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Customer(models.Model):
    customer = User.is_authenticated

    def __str__(self):
        return self.customer


class Product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(max_length=200)
    price = models.DecimalField(default=0, max_digits=100, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    is_sale = models.BooleanField(default=False)
    is_special = models.BooleanField(default=False)
    is_exists = models.BooleanField(default=True)
    sale_price = models.DecimalField(default=0, max_digits=100, decimal_places=0)
    picture = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    phone_number = models.CharField(max_length=13)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
