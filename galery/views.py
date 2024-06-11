from django.shortcuts import render, get_object_or_404, redirect
from .models import Fotografia
from users.views import login
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to access this page')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) 
    return render(request, 'galery/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galery/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to access this page')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if("buscar" in request.GET):
        nome_a_buscar = request.GET["buscar"]
        if(nome_a_buscar):
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galery/buscar.html', {"cards": fotografias})