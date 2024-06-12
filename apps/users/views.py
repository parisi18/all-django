from django.shortcuts import render, redirect
from apps.users.forms import LoginForm, SubscribeForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username=username, 
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"Hello {username}! You are now logged in.")
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials. Try again.')
            return redirect('login')


    return render(request, 'users/login.html', {'form': form})

def subscribe(request):
    form = SubscribeForm()

    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            
        
            username = form['username'].value()
            email = form['email'].value()
            password = form['password'].value()

            if(User.objects.filter(username=username).exists()):
                messages.error(request, 'Username already exists')
                return redirect('subscribe')
            
            user = User.objects.create_user(username, email, password)
            user.save()

            messages.success(request, 'You are now registered and can log in')
            return redirect('login')
            
    return render(request, 'users/subscribe.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')