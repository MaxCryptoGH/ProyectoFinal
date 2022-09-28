from django.contrib import admin

# Register your models here.
from .models import Perfil, Avatar


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "bio", "web")


admin.site.register(Avatar)
