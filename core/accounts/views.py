# accounts/views.py
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import VendorSignupForm, CustomerSignupForm

def vendor_signup(request):
    if request.method == 'POST':
        form = VendorSignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # Save the vendor user
            messages.success(request, 'Vendor account has been created successfully.')
            return redirect('home')  # Redirect after successful signup
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = VendorSignupForm()
    
    return render(request, 'registration/vendor_signup.html', {'form': form})

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # Save the customer user
            messages.success(request, 'Account has been created successfully.')
            return redirect('home')  # Redirect after successful signup
        else:
            messages.error(request, 'There were errors in your form. Please correct them and try again.')
    else:
        form = CustomerSignupForm()

    return render(request, 'registration/customer_signup.html', {'form': form})