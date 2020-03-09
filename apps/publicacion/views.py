from django.shortcuts import render

from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.urls import reverse, reverse_lazy

# Create your views here.

def publicar(request):
    return render(request, "publicar.html")