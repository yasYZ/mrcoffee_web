from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .models import Product
from django.http import JsonResponse

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


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        response = JsonResponse({'Product name': product.name})
        return response


def cart_del(request):
    return render(request, 'cart.html')


def cart_up(request):
    return render(request, 'cart.html')
