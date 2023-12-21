from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .models import Product, Order
from django.http import JsonResponse
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

    pass


def cart_up(request):
    return render(request, 'cart.html')


def cart_conf(request):
    form = Order

    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    context = {'form': form}
    return render(request, 'urlProduct/intPI/productSoldConfirm.html')
