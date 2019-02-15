from django import forms
from .models import Carrera, Entreno, Posicion

class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = ['nombre', 'distancia', 'plazas', 'fecha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'distancia': forms.NumberInput(attrs={'class':'form-control'}),
            'plazas': forms.NumberInput(attrs={'class':'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class':'form-control', 'type':'date'}),
        }

class EntrenoForm(forms.ModelForm):

    class Meta:
        model = Entreno
        fields = ['nombre', 'imagen', 'corredor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'corredor': forms.Select(attrs={'class':'form-control'}),
        }

class PosicionForm(forms.ModelForm):

    class Meta:
        model = Posicion
        fields = ['posicion']
        widgets = {
            'posicion': forms.TextInput(attrs={'class':'form-control'}),
        }