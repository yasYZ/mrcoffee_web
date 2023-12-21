from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url="/home", permanent=True)),
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('product/<int:pi>/', views.product_detail, name='products_detail'),
    path('cart/', views.__cart__, name='cart-summery'),
    path('cart/add/', views.cart_add, name='cart_add'),
    path('cart/delete', views.cart_del, name='cart-delete'),
    path('cart/update', views.cart_up, name='cart-update'),
    path('cart/confirm/', views.cart_conf, name='cart-update'),
]
