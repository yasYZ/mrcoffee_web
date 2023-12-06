from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('Products/', views.products, name='products'),
    # path('Products/<int:pk>', views.products, name='products'),
]
