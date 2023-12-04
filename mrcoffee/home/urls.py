from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url="/Home", permanent=True)),
    path('Home/', views.home, name='home'),
    path('ContactUs/', views.contact_us, name='contact_us'),
    path('AboutUs/', views.about_us, name='about_us')
]
