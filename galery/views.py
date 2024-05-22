from django.shortcuts import render

# Create your views here.



def index(request):

    dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org / NASA / James Webb"},
    2: {"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}
    }

    return render(request, 'galery/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galery/imagem.html')