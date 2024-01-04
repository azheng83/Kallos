from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class CustomLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    #class Meta:
        #model = get_user_model()
        #fields = [
            #'email',
            #'password'
        #]