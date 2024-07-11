from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    name = forms.CharField(max_length=100, help_text='Required. Enter your full name.')
    phone_number = forms.CharField(max_length=20, help_text='Required. Enter your phone number.')

    class Meta:
        model = User
        fields = ('email', 'name', 'phone_number', 'password1', 'password2')





def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home') 
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'newyear/login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. You can now login.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'newyear/register.html', {'form': form})
    