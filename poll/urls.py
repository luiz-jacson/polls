from django.urls import path
from poll.views import Create_poll, Home_view
urlpatterns = [
    path('', Home_view.as_view(), name = 'home'),
    path('create/', Create_poll, name='create'),
]