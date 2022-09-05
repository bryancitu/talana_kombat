from django.urls import path
from .views import *

urlpatterns = [
    path(
        'api/powers/',
        PowersApiView.as_view(),
        name='detail_power'
    ),
    path(
        'api/power/<int:pk>/',
        PowerDetailApiView.as_view(),
        name=''
    ),
    path(
        'api/players/',
        PlayersApiView.as_view(),
        name='players'
    ),
    path(
        'api/player/<int:pk>/',
        PlayerDetailApiView.as_view(),
        name='detail_player'
    ),
]
