from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia
from django.urls import reverse_lazy
from .forms import NoticiaForm
from django.shortcuts import redirect

class IsStaff(object):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(IsStaff, self). dispatch(request, *args, **kwargs)

class noticiasListView(ListView):
    model = Noticia
    template_name = 'noticias/noticias.html'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia.html'

class AddNoticia(IsStaff, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticiaform.html'
    success_url = reverse_lazy('noticias:noticias')

class EditNoticia(IsStaff, UpdateView):
    model = Noticia
    fields = ['titulo', 'contenido', 'descripcion', 'imagen']
    template_name = 'noticias/editnoticia.html'
    success_url = reverse_lazy('noticias:noticias')

class NoticiaDelete(IsStaff, DeleteView):
    model = Noticia
    template_name = 'noticias/confirmdeletenoticia.html'
    success_url = reverse_lazy('noticias:noticias')