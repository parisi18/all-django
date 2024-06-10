from django.shortcuts import render, redirect
from users.forms import LoginForm, SubscribeForm
from django.contrib.auth.models import User

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def subscribe(request):
    form = SubscribeForm()

    if request.method == 'POST':
        form = SubscribeForm(request.POST)

        if form.is_valid():
            if form["password"].value() != form["password_confirm"].value():
                return redirect('subscribe')
        
            username = form['username'].value()
            email = form['email'].value()
            password = form['password'].value()

            if(User.objects.filter(username=username).exists()):
                return redirect('subscribe')
            
            user = User.objects.create_user(username, email, password)
            user.save()

            return redirect('login')
            
    return render(request, 'users/subscribe.html', {'form': form})