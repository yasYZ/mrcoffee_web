from django.shortcuts import render, redirect

from .models import Product


# Create your views here.


def products(request):
    all_product = Product.objects.all()
    return render(request, 'Products.html', {'products': all_product})


def product_detail(request, pi):
    product = Product.objects.filter(id=pi)
    return render(request, 'productdetail.html', {'details': product})
