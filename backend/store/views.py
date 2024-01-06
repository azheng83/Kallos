from django.shortcuts import render
from .models import *

def Dashboard(request):
    context = {}
    return render(request, 'store/main.html', context)

def Basket(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

    context = {'items': items, 'order': order}
    return render(request, 'store/basket.html', context)

def Checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
