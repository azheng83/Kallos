from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegistrationForm, CustomLoginForm

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
    form = CustomLoginForm()
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email = email, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, f'Invalid login: Email - {email}, Password - {password}')
    
    return render(request, 'custom_user/login_user.html', {'form': form})

def LogoutUser(request):
    logout(request)
    return redirect('dashboard')





