from django import forms

class FormContactos(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField(required=False)
    mensaje = forms.CharField()