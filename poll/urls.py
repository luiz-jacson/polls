from django.urls import path
from poll.views import Create_poll, Home, Respostas, Resultados
urlpatterns = [
    path('', Home, name = 'home'),
    path('create/', Create_poll, name='create'),
    path('vote/<int:pk>/', Respostas, name = 'vote'),
    path('results/<int:pk>/', Resultados, name = 'result'),
]