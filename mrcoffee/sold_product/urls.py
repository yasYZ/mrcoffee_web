from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/<int:pi>/', views.product_detail, name='products_detail'),
]
