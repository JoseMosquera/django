from django.shortcuts import render, HttpResponseRedirect, render_to_response
from .forms import ContactoForm
from django.core.mail import EmailMessage
from .models import Contacto

def email(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            mail = EmailMessage(asunto, mensaje, to=['josemosquera96@gmail.com'])
            mail.send()
            em_autor=request.user
            em_asunto=form.cleaned_data['asunto']
            em_mensaje=form.cleaned_data['mensaje']
            contacto=Contacto(autor=em_autor, asunto=em_asunto, mensaje=em_mensaje)
            contacto.save()
            envio = "Mensaje enviado correctamente."
            newform=ContactoForm()
            return render(request, 'contacto/contacto.html', {'form':newform, 'envio':envio})
        else:
            form=ContactoForm()
            error = "error"
            return render(request, 'contacto/contacto.html', {'form':form, 'error':error})
    else:
        form=ContactoForm()
        return render(request, 'contacto/contacto.html', {'form':form})