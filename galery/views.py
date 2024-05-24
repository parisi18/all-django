from django.shortcuts import render, get_object_or_404
from .models import Fotografia


def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) 
    return render(request, 'galery/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galery/imagem.html', {"fotografia": fotografia})

def buscar(request):
    return render(request, 'galery/buscar.html')