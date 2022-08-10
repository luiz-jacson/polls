from django.urls import path
from poll.views import Create_poll, Home, Respostas, Resultados,Home_pagina
urlpatterns = [
    path('', Home, name = 'home'),
    path('home/<int:pagina>/', Home_pagina, name = 'home_pagina'),
    path('create/', Create_poll, name='create'),
    path('vote/<int:pk>/', Respostas, name = 'vote'),
    path('results/<int:pk>/', Resultados, name = 'result'),
]