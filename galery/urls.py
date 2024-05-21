from django.urls import path
from galery.views import index, image

urlpatterns = [
    path('', index),
    path('image/', image)
]