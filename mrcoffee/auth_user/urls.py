from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('LoginSignup/', views.login_register, name="LoginSignup"),
    path('Register/', views.register, name="Register"),
    path('Logout/', views.log_out, name="Logout"),
    path('ForgotPassword/', views.forgot_password, name="forgot_password"),
    path('ResetPassword/<str:uidb64>/<str:token>/', views.reset_password, name="reset_link"),
    path('ResetPasswordDone/', views.reset_password_done, name="reset_password_done_pg"),
    path('ForgetPasswordDone/', views.forgot_password_done, name="forget_password_done_pg"),
]