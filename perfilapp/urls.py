from django.urls import path
from perfilapp import views
from perfilapp.views import SignOutView
from perfilapp.views import SignInView, SignUpView, BienvenidaView


urlpatterns = [

    path("iniciar_sesion/", SignInView.as_view(), name="sign_in"),
    path("bienvenida/", BienvenidaView.as_view(), name="bienvenida"),
    path("cerrar-sesion/", SignOutView.as_view(), name="sign_out"),
    path("registrate/", SignUpView.as_view(), name="sign_up"),

]
