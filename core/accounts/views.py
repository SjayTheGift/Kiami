# accounts/views.py
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash, login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Address

from .forms import (
    VendorSignupForm, 
    CustomerSignupForm, 
    LoginForm , 
    ProfileUpdateForm,
    ChangePasswordForm,
    AddressForm,
    )

def login_view(request):
    if not request.user.is_authenticated:
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
    return redirect('home')

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


def account_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # Save the user profile
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')  # Redirect after successful update
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

def change_password_view(request):
    if request.method == "POST":
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()  # Save the new password
            update_session_auth_hash(request, user=request.user)  # Keep the user logged in
            messages.success(request, 'Password updated successfully.')
            return redirect('password_change')  # Redirect after successful update
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = ChangePasswordForm(user=request.user)  # Pass user to the form
    return render(request, 'accounts/change_password.html', {'form': form})

@login_required
def address(request):
    addresses = Address.objects.filter(user=request.user).all()
    return render(request, 'settings/address.html', {"addresses": addresses})

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, "Address added successfully!")
            return redirect('address_book')
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = AddressForm()
    return render(request, 'settings/add_address.html', {'form': form})

@login_required
def update_address(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, "Address updated successfully!")
            return redirect('address_book')
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = AddressForm(instance=address)
    return render(request, 'settings/update_address.html', {'form': form})

@login_required
def delete_address(request, pk):
   address = get_object_or_404(Address, pk=pk, user=request.user)
   if request.method == 'POST':
        address.delete()
        messages.success(request, "Address deleted successfully!")
        return redirect('address_book')
   return JsonResponse({'address': address})