from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('register', RegisterView.as_view(), name='register_page'),
    path('logout', LogoutView.as_view(), name='logout_page'),
    path('forget-pass', ForgetPasswordView.as_view(), name='forget_password_page'),
]