from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # Add an additional email field to the form
    email = forms.EmailField()

    class Meta:
        # Set the model to User, indicating that this form is used to create User instances
        model = User
        # Specify the fields to be included in the form
        fields = ['username', 'email', 'password1', 'password2']