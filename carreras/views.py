from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Carrera, Posicion, Entreno
from carreras.forms import CarreraForm, EntrenoForm, PosicionForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

#Carreras
def carreras(request):
    carreras = Carrera.objects.all()
    users = User.objects.all()
    return render(request, "carreras/carreras.html", {'carreras':carreras, 'users':users})

def addCarrera(request):
    if(request.method=='POST'):
        form=CarreraForm(request.POST, request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            ca_nombre=cd['nombre']
            ca_distancia=cd['distancia']
            ca_plazas=cd['plazas']
            ca_fecha=cd['fecha']
            carrera=Carrera(nombre=ca_nombre, distancia=ca_distancia, plazas=ca_plazas, fecha=ca_fecha)
            carrera.save()
            envio = "correcto"
            carreras = Carrera.objects.all()
            return render(request, 'carreras/carreras.html', {'envio':envio, 'carreras':carreras})
    else:
        form=CarreraForm()
    return render(request, 'carreras/addcarrera.html',{'form':form})

class EditCarrera(UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'carreras/editcarrera.html'

    def get_success_url(self):
        return reverse_lazy('carreras')

class CarreraDelete(DeleteView):
    model = Carrera
    template_name = 'carreras/deletecarrera.html'
    success_url = reverse_lazy('carreras')

#Apuntarse a carrera
def posicionesUser(request):
    posiciones = Posicion.objects.filter(user=request.user)
    return render(request, 'carreras/posicionesuser.html', {'posiciones':posiciones})

def posiciones(request):
    user_id = request.POST['userPosicion']
    posiciones = Posicion.objects.filter(user=user_id)
    return render(request, 'carreras/posiciones.html', {'posiciones':posiciones})

def addPosicion(request, carrera_id):
    pos_carrera=Carrera.objects.get(id=carrera_id)
    carrera = pos_carrera
    if (Posicion.objects.filter(user = request.user, carrera = pos_carrera)):
        repetido = "estas apuntado ya"
        carreras = Carrera.objects.all()
        return render(request, 'carreras/carreras.html', {'repetido':repetido, 'carreras':carreras})
    else:
        if (int(carrera.plazas) > 0):
            pos_user=request.user
            posicion=Posicion(carrera=pos_carrera, user=pos_user)
            posicion.save()
            carrera = pos_carrera
            plazas = int(carrera.plazas)
            plazas -= 1
            carrera.plazas = plazas
            carrera.save()
            apuntado = "correcto"
            carreras = Carrera.objects.all()
            return render(request, 'carreras/carreras.html', {'apuntado':apuntado, 'carreras':carreras})
        else:
            maximo = "maximo completado"
            return render(request, 'carreras/carreras.html', {'maximo':maximo, 'carreras':carreras})

class EditPosicion(UpdateView):
    model = Posicion
    form_class = PosicionForm
    template_name = 'carreras/posicionform.html'

    def get_success_url(self):
        return reverse_lazy('carreras')

#Entrenos
def entrenos(request):
    if (request.user.is_staff):
        entrenos = Entreno.objects.all()
        usuarios = User.objects.all()
        return render(request, 'carreras/entrenos.html', {'entrenos':entrenos, 'usuarios':usuarios})
    else:
        entrenos = Entreno.objects.filter(corredor=request.user)
        return render(request, 'carreras/entrenos.html', {'entrenos':entrenos})

def entrenosUser(request):
    entrenos = Entreno.objects.filter(corredor=request.POST['userEntrenos'])
    usuarios = User.objects.all()
    return render(request, 'carreras/entrenos.html', {'entrenos':entrenos, 'usuarios':usuarios})

def addEntreno(request):
    if(request.method=='POST'):
        form=EntrenoForm(request.POST, request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            e_nombre=cd['nombre']
            e_imagen=cd['imagen']
            e_corredor=cd['corredor']
            entreno=Entreno(nombre=e_nombre, imagen=e_imagen, corredor=e_corredor)
            entreno.save()
            envio = "correcto"
            usuarios = User.objects.all()
            entrenos = Entreno.objects.all()
            return render(request, 'carreras/entrenos.html', {'envio':envio, 'entrenos':entrenos, 'usuarios':usuarios})
    else:
        form=EntrenoForm()
    return render(request, 'carreras/addentreno.html',{'form':form})

class EditEntreno(UpdateView):
    model = Entreno
    form_class = EntrenoForm
    template_name = 'carreras/editentreno.html'

    def get_success_url(self):
        return reverse_lazy('entrenos')

class EntrenoDelete(DeleteView):
    model = Entreno
    template_name = 'carreras/entrenodelete.html'
    success_url = reverse_lazy('entrenos')
