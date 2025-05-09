from django.shortcuts import render

# Create your views here.

def home(request):
    food_items = "food"
    return render(request, 'home.html', {'food_items': food_items})

def food_list(request):
    food_items = "food"
    return render(request, 'food.html', {'food_items': food_items})

def food_details(request, id):
    food_items = "food"
    return render(request, 'food_details.html', {'food_items': food_items})