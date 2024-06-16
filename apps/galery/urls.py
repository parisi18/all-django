from django.urls import path
from apps.galery.views import *

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('new-image', new_image, name='new-image'),
    path('edit-image/<int:foto_id>', edit_image, name='edit-image'),
    path('delete-image', delete_image, name='delete-image')
]