from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'^formulario-buscar/$', views.formulario_buscar),
    url(r'buscar/$', views.buscar),
]
