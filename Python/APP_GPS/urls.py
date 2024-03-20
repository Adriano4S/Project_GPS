from django.urls import path
from .views import index, gps, abordagem, di, speech, fechamento, live, referidos

app_name = 'APP_GPS'

urlpatterns = [
    path('', index, name='index'),
    path('gps/', gps, name='gps'),
    path('abordagem/', abordagem, name='abordagem'),
    path('di/', di, name='di'),
    path('speech/', speech, name='speech'),
    path('fechamento/', fechamento, name='fechamento'),
    path('live/', live, name='live'),
    path('referidos/', referidos, name='referidos'),
]

