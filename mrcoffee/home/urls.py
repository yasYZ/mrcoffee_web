from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url="/home", permanent=True)),
    path('home/', views.home, name='home'),
    path('contactUs/', views.contact_us, name='contact_us'),
    path('about-us/', views.about_us, name='about_us'),
]
