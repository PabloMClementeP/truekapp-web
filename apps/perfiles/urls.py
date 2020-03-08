from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordChangeDoneView
from apps.perfiles.views import Registrarse

urlpatterns = [
    path('registrarse/', Registrarse.as_view(), name='registrar'),
    path('ingreso/', LoginView.as_view(template_name ='login.html'),name='ingreso'),
    path('password_reset/', PasswordResetView.as_view(template_name ='password_reset.html'), name='resetpass'),
    path('done/', PasswordChangeDoneView.as_view(template_name ='password_reset_done.html'),name='password_reset_done'),
    path('<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name ='password_reset_confirm.html'),name='password_reset_confirm'),
    path('complete/', PasswordResetCompleteView.as_view(template_name ='password_reset_complete.html'),name='password_reset_complete'),
]

