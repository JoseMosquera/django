from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'descripcion', 'imagen', 'categorias']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'categorias': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['contenido', 'imagen']
        widgets = {
            'contenido': forms.Textarea(attrs={'class':'form-control'}),
        }