from django.urls import path
from api_rest.views import detalle_menor, listado_apoderados, listado_menores, modEliminarApoderado, listado_cuidadores, modEliminarCuidador
from api_rest.viewsLogin import ini_user

urlpatterns = [
    path('listado_apoderados/',listado_apoderados,name="listado_apoderados"),
    path('modEliminarApoderado/<rut>',modEliminarApoderado,name="modEliminarApoderado"),
    path('listado_cuidadores/',listado_cuidadores,name="listado_cuidadores"),
    path('modEliminarCuidador/<rut>',modEliminarCuidador,name="modEliminarCuidador"),
    path('listado_menores/',listado_menores,name="listado_menores"),
    path('detalle_menor/<rut>',detalle_menor,name="detalle_menor"),
    path('ini_user/',ini_user,name="ini_user"),
    ]