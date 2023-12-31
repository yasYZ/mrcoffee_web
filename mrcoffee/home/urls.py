from django.urls import path
from . import views


urlpatterns = [
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
    path('email-confirm/', views.mail_confirm, name='mail_confirm'),
]
