from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .cart import Cart
from .models import Product, Order, Category
from django.http import JsonResponse, HttpResponse
from .context_processors import cart

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


def __cart__(request):
    cart = Cart(request).cart
    print({'products': cart})
    return render(request, 'cart.html', {'products': cart})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        amount = request.POST.get('amount')
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, amount=amount)

        response = JsonResponse({'Product name': product.name, 'product_price': product.price})

        return response


def cart_del(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        response = JsonResponse({'Product name': product.name, 'product_price': product.price})
        cart.delete(product=product_id)

        return response


def cart_conf(request):
    cart = Cart(request).cart
    id_keys = cart.keys()
    total_price = 0

    for item in id_keys:
        item = cart[item]
        price_str = item.get('price', '0')
        price_int = int(price_str)

        total_price += price_int

    if request.method == 'POST':
        if User.is_authenticated:
            phone_number = request.POST.get('ph_number')
            mail = request.POST.get('mail')
            address = request.POST.get('address')
            Order.objects.create(phone_number=phone_number, product=cart, customer=request.user, mail=mail, address=address)
            return HttpResponse('<h1>پرداخت موفق</h1>''<h2>کاربران ما تا 24 ساعت آینده به شما ایمیل یا پیامک ارسال میکنند</h2>')
        else:
            redirect('/login-signup')
    return render(request, 'urlProduct/intPI/productSoldConfirm.html', {'products': cart, 'sum_total_price': str(total_price)})
