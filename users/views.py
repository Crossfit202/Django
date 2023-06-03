from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = UserRegisterForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the form data and create a new user
            form.save()
            # Retrieve the username from the form data
            username = form.cleaned_data.get('username')
            # Display a success message using Django's messages framework
            messages.success(request, f'Your account has been created. You are now able to log in!')
            # Redirect the user to the login page
            return redirect('login')
    else:    
        # If the request method is not POST, create a new blank form
        form = UserRegisterForm()
    
    # Render the registration template with the form data
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    # Render the profile template
    return render(request, 'users/profile.html')
