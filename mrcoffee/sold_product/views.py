from django.shortcuts import render, redirect

from .models import Product


# Create your views here.


def home(request):
    all_product = Product.objects.all()
    return render(request, 'index.html', {'products': all_product})


def products(request):
    all_product = Product.objects.all()
    return render(request, 'Products.html', {'products': all_product})


def product_detail(request, pi):
    product = Product.objects.filter(id=pi)
    return render(request, 'urlProduct/intPI/productdetail.html', {'details': product})


def cart(request):
    return render(request, 'cart.html')
