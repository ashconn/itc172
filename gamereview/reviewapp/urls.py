from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gametype/', views.gametype, name='gametype'),
    path('game/', views.game, name='game'),
    path('review/', views.review, name='review'),
    path('newgame/', views.newgame, name='newgame'),
    path('newreview/', views.newreview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]