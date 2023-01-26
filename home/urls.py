from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('contact', contact, name ='contact'),
    path('blog', blog, name ='blog'),
    path('matches', match, name ='matches'),
    path('players', player, name ='players'),
    path('single', single, name ='single'),

]