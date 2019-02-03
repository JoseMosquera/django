from django import forms
from .models import Carrera, Entreno

class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = ['nombre', 'distancia', 'plazas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'distancia': forms.Textarea(attrs={'class':'form-control'}),
            'plazas': forms.Textarea(attrs={'class':'form-control'}),
        }

class EntrenoForm(forms.ModelForm):

    class Meta:
        model = Entreno
        fields = ['nombre', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }