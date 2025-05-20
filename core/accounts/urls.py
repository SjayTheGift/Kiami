# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    vendor_signup_view, 
    customer_signup_view, 
    login_view, 
    account_view,
    address,
    add_address,
    update_address,
    delete_address,
    change_password_view,
    set_default_address,
    )

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('vendor/signup/', vendor_signup_view, name='vendor_signup'),
    path('customer/signup/', customer_signup_view, name='customer_signup'),
    path('profile/', account_view, name='profile'),
    path('address-book/', address, name='address_book'),
    path('address-book/add/', add_address, name='address_book_add'),
    path('address-book/update/<int:pk>/', update_address, name='address_book_update'),
    path('address-book/delete/<int:pk>/', delete_address, name='address_book_delete'),
    path('address-book/default/<int:pk>/', set_default_address, name='set_default_address'),

    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), 
        name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    path('password-change/',  change_password_view, name='password_change'),
]