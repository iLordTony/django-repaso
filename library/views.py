# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
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


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('asunto', ''):
            errors.append('Por favor introduce el asunto.')
        if not request.POST.get('mensaje', ''):
            errors.append('Por favor introduce un mensaje.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de email valida.')
        if not errors:
            send_mail(request.POST['asunto'], request.POST['mensaje'], request.POST.get('email', 'noreply@example.com'), ['siteowner@example.com'],)
            return HttpResponseRedirect('/contactos/gracias/')
    return render(request, 'formulario-contactos.html', {'errors': errors,
                                                         'asunto': request.POST.get('asunto', ''),
                                                         'mensaje': request.POST.get('mensaje', ''),
                                                         'email': request.POST.get('email', '')})