from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path("mostrar_resultado", recuperar, name='mostrar_resultado'),
	path("iniciarsesion/", iniciarsesion, name='iniciarsesion'),
	path("contacto/", contacto, name='contacto'),
	path("catalogo/", catalogo, name='catalogo'),
	path("carro/", carro, name='carro'),
	path("config/", configuracion, name='config'),
]