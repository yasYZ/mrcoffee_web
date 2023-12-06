from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('Products/', views.products, name='products'),
    path('Product<int:pi>/', views.product_detail, name='products_detail'),
]
