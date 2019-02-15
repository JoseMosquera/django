from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User, Group

class HomePageView(TemplateView):
    template_name = "nucleo/home.html"

def usuarios(request):
    usuarios = User.objects.filter(groups = None).order_by('first_name')
    return render(request, "nucleo/usuarios.html", {'usuarios':usuarios})

def usuariosGroup(request):
    user_id = request.POST['user_id']
    usuario = User.objects.get(id=user_id)
    group = Group.objects.get(id=3)
    usuario.groups.add(group)
    usuarios = User.objects.filter(groups = None).order_by('first_name')
    return render(request, "nucleo/usuarios.html", {'usuarios':usuarios})