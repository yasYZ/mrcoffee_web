from django.shortcuts import render

# Create your views here.


def contact_us(request):
    return render(request, 'Contactus.html')


def about_us(request):
    return render(request, 'Aboutus.html')


def mail_confirm(request):
    return render(request, 'mailConfirm.html')
