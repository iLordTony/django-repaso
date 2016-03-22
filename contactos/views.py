from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from contactos.forms import FormContactos


def contact(request):
    if request.method == 'POST':
        form = FormContactos(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['asunto'],
                      cd['mensaje'],
                      cd.get('email', 'noreply@example.com'),
                      ['siteowner@example.com'],)
            return HttpResponseRedirect('/contactos/gracias/')
    else:
        form = FormContactos(initial={'asunto': 'Hello Moy'})
    return render(request, 'formulario-contactos.html', {'form': form})