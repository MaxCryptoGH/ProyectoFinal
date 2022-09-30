from django.urls import path
from blogapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('about/', views.about,  name="about"),
    path('crear_articulo/', views.articulo, name='crear_articulo'),
    path('blog/', views.blog, name='blog'),
    path('eliminar_art/<id>/', views.eliminar_art, name='eliminar_art'),
    path('borrado/', views.borrado, name='borrado'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
