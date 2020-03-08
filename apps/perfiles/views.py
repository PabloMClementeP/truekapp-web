from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse, reverse_lazy

from apps.perfiles.forms import RegistrarseForm
from apps.perfiles.models import Perfil

# Create your views here.

class Registrarse(CreateView):
    model = User
    template_name = 'registrarse.html'
    form_class = RegistrarseForm
    success_url = reverse_lazy('home')

#class Login(TemplateView):
#	template_name = 'login.html'
#	success_url = reverse_lazy('home')



