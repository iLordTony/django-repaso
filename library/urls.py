from django.conf.urls import url
from library import views

urlpatterns = [
    url(r'buscar/$', views.buscar),
    url(r'contact/$', views.contact)
]
