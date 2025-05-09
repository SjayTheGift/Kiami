# accounts/urls.py
from django.urls import path
from .views import vendor_signup, customer_signup

urlpatterns = [
    path('vendor/signup/', vendor_signup, name='vendor_signup'),
    path('customer/signup/', customer_signup, name='customer_signup'),
]