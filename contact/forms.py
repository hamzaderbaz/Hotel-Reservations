from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile

# Form for user signup using UserCreationForm
class SignupForm(UserCreationForm):
    class Meta:
        model = User  # Using the User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields required for signup




# Form for updating User model fields
class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Using the User model
        fields = ['username', 'first_name', 'last_name', 'email']  # Fields for updating user details


# Form for updating Profile model fields
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Using the Profile model
        fields = ['city', 'phone_number', 'image']  # Fields for updating profile details




class LoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ['username', 'password1']
