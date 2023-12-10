from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('login-signup/', views.login_register, name="LoginSignup"),
    path('register/', views.register, name="Register"),
    path('logout/', views.log_out, name="Logout"),
    path('forgot-password/', views.forgot_password, name="forgot_password"),
    path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name="reset_link"),
    path('reset-password-done/', views.reset_password_done, name="reset_password_done_pg"),
    path('forget-password-done/', views.forgot_password_done, name="forget_password_done_pg"),
]