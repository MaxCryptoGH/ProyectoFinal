from django.urls import path
from blogapp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about/', views.about,  name="about"),
    path('crear_articulo/', views.articulo, name='crear_articulo'),
    path('mostrarArticulo/', views.mostrarArticulo, name='blog'),

]
