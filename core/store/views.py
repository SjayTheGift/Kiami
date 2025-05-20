from django.shortcuts import render

# Create your views here.

def home_view(request):
    food_items = "food"
    return render(request, 'home.html', {'food_items': food_items})

def food_list_view(request):
    food_items = "food"
    return render(request, 'food.html', {'food_items': food_items})

def food_details_view(request, id):
    food_items = "food"
    return render(request, 'food_details.html', {'food_items': food_items})

def cart_view(request):
    return render(request, 'cart.html')

def orders_view(request):
    return render(request, 'orders/orders.html')

def orders_details_view(request, pk):
    return render(request, 'orders/order_details.html')