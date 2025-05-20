from django.urls import path
from .views import (
    food_list_view, 
    home_view, 
    food_details_view,
    cart_view,
    orders_view,
    orders_details_view,
)

urlpatterns = [
    path('', home_view, name="home"),
    path('food/', food_list_view, name="food_list"),
    path('food/<int:id>/', food_details_view, name="food_details"),
    path('cart/', cart_view, name="cart"),
    path('orders/', orders_view, name="orders_list"),
    path('orders/<int:pk>/', orders_details_view, name="orders_details"),
]
