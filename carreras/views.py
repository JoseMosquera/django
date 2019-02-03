from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Carrera, Posicion, Entreno
from carreras.forms import CarreraForm, EntrenoForm 
from django.urls import reverse_lazy, reverse
    
def carreras(request):
    carreras = Carrera.objects.all()
    return render(request, "carreras/carreras.html", {'carreras':carreras})

# def addCarrera(request):
#      if(request.method=='POST'):
#         form=carreraAdd(request.POST, request.FILES)
#         if form.is_valid():
#             cd=form.cleaned_data
#             ca_nombre=cd['nombre']
#             ca_distancia=cd['distancia']
#             ca_plazas=cd['plazas']
#             ca_imagen=cd['imagen']
#             ca_autor=request.user
#             ca_foro=Foro.objects.get(id=foro_id)
#             ca_categorias=cd['categorias']
#             post=Post(nombre=ca_nombre, distancia=ca_distancia, plazas=ca_plazas, imagen=ca_imagen, autor=ca_autor, foro=ca_foro)
#             post.save()
#             post.categorias.set(ca_categorias)
#             return HttpResponseRedirect(reverse('posts', args=[foro_id]))
#     else:
#         form=PostForm()
#     return render(request, 'blog/categoria.html',{'form':form})

def entrenos(request):
    entrenos = Entreno.objects.all()
    return render(request, 'carreras/entrenos.html', {'entrenos':entrenos})