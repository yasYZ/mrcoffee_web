from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'Contactus.html')


def about_us(request):
    return render(request, 'Aboutus.html')