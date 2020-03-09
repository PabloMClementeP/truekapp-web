from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('publicar/', login_required(views.publicar), name='publicar'),
]
