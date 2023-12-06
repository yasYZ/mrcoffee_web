from django.shortcuts import render

from .models import Product


# Create your views here.


def products(request):
    all_product = Product.objects.all()
    return render(request, 'products.html', {'products': all_product})


def product_detail(request, pi):
    details = Product.objects.get(pk=pi)
    return render(request, 'product_det.html', {'detail': details})
