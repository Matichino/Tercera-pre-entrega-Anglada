from django import forms

class ClienteFormulario(forms.Form):
    usuario = forms.CharField(label="Nombre de Usuario", max_length=8)
    numero_de_caso = forms.IntegerField(label="Número de Caso")

