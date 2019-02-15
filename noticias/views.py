from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Noticia
from django.urls import reverse_lazy
from .forms import NoticiaForm
from django.shortcuts import redirect

class noticiasListView(ListView):
    model = Noticia
    template_name = 'noticias/noticias.html'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia.html'

class AddNoticia(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticiaform.html'

    def get_success_url(self):
        return reverse_lazy('noticias:noticias') + '?correcto'

class EditNoticia(UpdateView):
    model = Noticia
    fields = ['titulo', 'contenido', 'descripcion', 'imagen']
    template_name = 'noticias/editnoticia.html'
    success_url = reverse_lazy('noticias:noticias')

class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = 'noticias/confirmdeletenoticia.html'
    success_url = reverse_lazy('noticias:noticias')