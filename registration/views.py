from .forms import UserWithEmail, PerfilForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Perfil

class SingUpView(CreateView):
    form_class = UserWithEmail
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo electronico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repita su contraseña'})

        return form

@method_decorator(login_required, name='dispatch')
class PerfilUpdate(UpdateView):
    form_class = PerfilForm
    success_url = reverse_lazy('perfil')
    template_name = 'registration/perfilform.html'

    def get_object(self):
        perfil, create = Perfil.objects.get_or_create(user=self.request.user)
        return perfil