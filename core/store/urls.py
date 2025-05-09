from django.urls import path
from .views import food_list, home, food_details
urlpatterns = [
    path('', home, name="home"),
    path('food/', food_list, name="food"),
    path('food/<int:id>/', food_details, name="food_details"),
]
