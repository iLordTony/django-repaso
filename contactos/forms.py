# coding=utf-8
from django import forms


class FormContactos(forms.Form):
    asunto = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Tu correo plis')
    mensaje = forms.CharField(widget=forms.Textarea)

    # Siempre que vea algo como clean_nombre_del_campo django lo ejecuta como otra validacion
    def clean_mensaje(self):
        mensaje = self.cleaned_data['mensaje']
        num_palabras = len(mensaje.split())

        if num_palabras < 4:
            raise forms.ValidationError("¡Se requieren mínimo 4 palabras!")
        return mensaje # siempre retornar el valor original
