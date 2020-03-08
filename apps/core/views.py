from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "inicio.html")

def ayuda(request):
    return render(request, "ayuda.html")