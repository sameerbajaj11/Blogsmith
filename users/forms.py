from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# We'll use this form as our user registration form instead of UserCreationForm
class UserRegisterForm(UserCreationForm):

    # by default, required is true in emailfield
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Whenever we put both of these on one template, this is going to look like one

class UserUpdateForm(forms.ModelForm):

    # by default, required is true in emailfield
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
