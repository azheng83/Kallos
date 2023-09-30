from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import RegistrationForm

def RegisterUser(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            form.save()
            messages.success(request, 'Success!')
            new_user = authenticate(username = username, password = password1)
            if new_user is not None:
                login(request, new_user)

        else:
            messages.error(request, 'failure')

    return render(request, 'registerUser/registeruser.html', {'form': form})
