from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def formulario_buscar(request):
    return render(request, 'formulario_buscar.html')

def buscar(request):
    if 'q' in request.GET and request.GET['q']:
        msn = 'Estas buscando: %r' % request.GET['q']
    else:
        msn = 'Formulario vacio =('

    return HttpResponse(msn)