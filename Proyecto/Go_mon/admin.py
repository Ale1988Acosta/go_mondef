from django.contrib import admin
from .models import Habilidad, Cuidador, Region, Comuna, Direc_Cuidador, Direc_Apoderado, Sexo, Habil_cuid,Idioma, Idio_cuid, Dia, Bloque, Dia_Bloq, Menor, Apoderado, Servicio, Servi_Bloq, Rol, Usuario

# Register your models here.
admin.site.register(Habilidad)
admin.site.register(Cuidador)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direc_Cuidador)
admin.site.register(Direc_Apoderado)
admin.site.register(Sexo)
admin.site.register(Habil_cuid)
admin.site.register(Idioma)
admin.site.register(Idio_cuid)
admin.site.register(Dia)
admin.site.register(Bloque)
admin.site.register(Dia_Bloq)
admin.site.register(Menor)
admin.site.register(Apoderado)
admin.site.register(Servicio)
admin.site.register(Servi_Bloq)
admin.site.register(Rol)
admin.site.register(Usuario)