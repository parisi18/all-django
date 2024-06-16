from django.shortcuts import render, get_object_or_404, redirect
from apps.galery.models import Fotografia
from apps.galery.forms import FotografiaForm
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

def new_image(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to access this page')
        return redirect('login')
        
    form = FotografiaForm()

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image successfully added')
            return redirect('index')
        else:
            return render(request, 'galery/new_image.html',  {'form': form})

    return render(request, 'galery/new_image.html',  {'form': form})

def edit_image(request, foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image successfully edited')
            return redirect('index')
        else:
            return render(request, 'galery/edit_image.html', {'form': form, 'foto_id': foto_id})

    return render(request, 'galery/edit_image.html', {'form': form, 'foto_id': foto_id})


def delete_image(request):
    pass