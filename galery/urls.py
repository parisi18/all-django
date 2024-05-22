from django.urls import path
from galery.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]