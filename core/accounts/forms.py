from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm ,PasswordChangeForm
from .models import User

from django import forms
from .models import User, Address

class LoginForm(AuthenticationForm):  # Inherit from forms.Form, not AuthenticationForm
    username = forms.EmailField(label="Email")
    

class VendorSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    phone = forms.CharField(max_length=14, required=True, label="Phone Number")
    email = forms.EmailField(max_length=150, required=True, label="Email")
    password2 = forms.CharField(max_length=150, label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'password1', 'password2']  # Use password1 and password2 from UserCreationForm

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_vendor = True
        if commit:
            user.save()
        return user

class CustomerSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="First Name")
    last_name = forms.CharField(max_length=100, required=True, label="Last Name")
    phone = forms.CharField(max_length=14, required=True, label="Phone Number")
    email = forms.EmailField(max_length=150, required=True, label="Email")
    password2 = forms.CharField(max_length=150, label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'password1', 'password2']  # Use password1 and password2 from UserCreationForm

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        return user
    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)

class ProfileUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'middle_name', 'phone', 'email')

class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = []


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'suburb', 'city', 'province', 'postal_code'] 

