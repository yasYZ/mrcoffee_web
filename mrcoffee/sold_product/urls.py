from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url="/home", permanent=True)),
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/<int:pi>/', views.product_detail, name='products_detail'),
    path('cart/', views.cart, name='cart-summery'),
    path('cart/add', views.cart, name='cart-add'),
    path('cart/delete', views.cart, name='cart-delete'),
    path('cart/update', views.cart, name='cart-update'),
]
