from django import forms

class addPost(forms.Form):
    titulo = forms.CharField(label="Titulo", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Titulo del post'}
    ), min_length=3, max_length=100)

    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Contenido del post'}
    ), min_length=10, max_length=1000)

    descripcion = forms.CharField(label="Descripcion", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Descripcion del post'}
    ), min_length=10, max_length=1000)