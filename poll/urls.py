from django.urls import path
from poll.views import Create_poll
urlpatterns = [
    path('create/', Create_poll, name='create')
]