from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
import datetime


def hola(request):
    return HttpResponse('Hola mundo')


def raiz(request):
    return HttpResponse('Raiz')


def fecha_actual(request):
    ahora = datetime.datetime.now()
    # Esta forma no esta chida aun
    # t = get_template('fecha_actual.html')
    # html = t.render(Context({'fecha_actual': ahora}))
    # return HttpResponse(html)
    # Esta es la buena
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})


def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body><h1>En %s hora(s), seran:</h1><h3>%s</h3></body></html>" % (offset, dt)
    return HttpResponse(html)
