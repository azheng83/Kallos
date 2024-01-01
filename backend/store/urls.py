from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),
    path('basket/', views.Basket, name="basket"),
    path('checkout/', views.Checkout, name="checkout")
]