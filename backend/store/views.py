from django.shortcuts import render
from products.views import Perfume
from custom_user.views import LoginUser

def Dashboard(request):
    context = {}
    return render(request, 'store/main.html', context)

def Basket(request):
    context = {}
    return render(request, 'store/main.html', context)

