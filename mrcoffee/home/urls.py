from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url="/Home", permanent=True)),
    path('Home/', views.home),
]
