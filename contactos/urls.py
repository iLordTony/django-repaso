from django.conf.urls import url
from contactos import views

urlpatterns = [
    url(r'contact/$', views.contact)
]
