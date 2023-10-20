from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm

def RegisterUser(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            form.save()
            new_user = authenticate(request, email = email, password = password1)
            if new_user is not None:
                login(request, new_user)
                messages.success(request, 'Login successful!')

        else:
            messages.error(request, 'failure')

    return render(request, 'custom_user/register_user.html', {'form': form})

def LoginUser(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)

            messages.success(request, 'Successfully logged in!')
        
        else:
            messages.error(request, 'There is an error with your email and/or password.')
    
    return render(request, 'custom_user/login_user.html', {'form': form})



