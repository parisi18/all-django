from django.urls import path
from apps.users.views import *

urlpatterns = [
    path('login', login, name='login'),
    path('subscribe', subscribe, name='subscribe'),
    path('logout', logout, name='logout')
] 
