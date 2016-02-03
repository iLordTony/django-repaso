from django.http import HttpResponse, Http404
import datetime


def hola(request):
    return HttpResponse('Hola mundo')


def raiz(request):
    return HttpResponse('Raiz')


def fecha_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body><h1>Fecha:</h1><h3>%s</h3></body></html>" % ahora
    return HttpResponse(html)


def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    assert False
    html = "<html><body><h1>En %s hora(s), seran:</h1><h3>%s</h3></body></html>" % (offset, dt)
    return HttpResponse(html)
