# accounts/views.py
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import VendorSignupForm, CustomerSignupForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
           
            if user is not None:
                auth_login(request, user)
                return redirect('home') 
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def vendor_signup_view(request):
    if request.method == 'POST':
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # Save the vendor user
            messages.success(request, 'Vendor account has been created successfully.')
            return redirect('login')  # Redirect after successful signup
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = VendorSignupForm()
    
    return render(request, 'accounts/vendor_signup.html', {'form': form})

def customer_signup_view(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # Save the customer user
            messages.success(request, 'Account has been created successfully.')
            return redirect('login')  # Redirect after successful signup
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = CustomerSignupForm()

    return render(request, 'accounts/customer_signup.html', {'form': form})