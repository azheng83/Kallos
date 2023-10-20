from django.urls import path

from . import views

urlpatterns = [
    path("users-registration/", views.RegisterUser, name="register"),
    path("users-login/", views.LoginUser, name='login')
]