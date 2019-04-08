from django.urls import path, include
from aplicaciones.inicio.views import Inicio
urlpatterns = [
    path('', Inicio.as_view(), name='home' ),
]