from django.shortcuts import render

def login(request):
    return render(request, 'users/login.html')

def subscribe(request):
    return render(request, 'users/subscribe.html')