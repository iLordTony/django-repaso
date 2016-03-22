# coding=utf-8
from django.shortcuts import render

from library.models import Book


# Create your views here.


def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Por favor introduce un término de búsqueda.')
        elif len(q) > 20:
            errors.append('Por favor introduce un término de búsqueda menor a 20 caracteres.')
        else:
            books = Book.objects.filter(title__icontains=q) # icontains no importan las mayusculas o minusculas
            return render(request, 'resultados.html', {'books': books, 'query': q})

    return render(request, 'formulario-buscar.html', {'errors': errors})
