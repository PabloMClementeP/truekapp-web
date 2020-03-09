from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    contacto_form = ContactForm

    if request.method == "POST":
        contacto_form = contacto_form(data=request.POST)
        if contacto_form.is_valid():
            nombre = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            mensaje = request.POST.get('mensaje', '')

            #Envio de correo y redireccion
            email = EmailMessage(
                "Nuevo mensaje de Truekapp Ayuda",                              # asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(nombre, email, mensaje), # cuerpo
                "no-contestar-truekap@gmail.com",                               # email origen
                ["truekappweb@gmail.com"],                                      # email destino
                reply_to=[email]                                                # correo de quien envia
            )
            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")    
            except:
                #Algo ha salido mal
                return redirect(reverse('contacto')+"?Fail")
            
    return render(request, "ayuda.html", {'form':contacto_form})