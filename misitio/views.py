import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render


def hola(request):
    return HttpResponse('Hola mundo')


def raiz(request):
    return HttpResponse('Raiz')


def fecha_actual(request):
    ahora = datetime.datetime.now()
    # Esta forma no esta chida aun
    # t = get_template('fecha-actual.html')
    # html = t.render(Context({'fecha_actual': ahora}))
    # return HttpResponse(html)
    # Esta es la buena
    return render(request, 'fecha-actual.html', {'fecha_actual': ahora})


def horas_adelante(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'horas-adelante.html', {'fecha_adelante': dt, 'horas': offset})


def atributos_meta(request):
    valor = request.META.items()
    valor.sort()

    return render(request, 'atributos.html', {'valor': valor})