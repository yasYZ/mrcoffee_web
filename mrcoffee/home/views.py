from django.shortcuts import render

# Create your views here.


def home(request):
    # product = Product.object.all()
    return render(request, 'htmls/Fa/index.html')


def contact_us(request):
    return render(request, 'htmls/Fa/Contactus.html')


def about_us(request):
    return render(request, 'htmls/Fa/Aboutus.html')


def products(request):
    return render(request, 'htmls/Fa/Products.html')
