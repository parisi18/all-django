from django.shortcuts import render
from users.forms import LoginForm, SubscribeForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def subscribe(request):
    form = SubscribeForm()
    return render(request, 'users/subscribe.html', {'form': form})