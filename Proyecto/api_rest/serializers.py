from rest_framework import serializers
from Go_mon.models import Apoderado, Cuidador, Menor

class ApoderadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apoderado
        fields = ['rut_apoderado','nombre','p_apellido','s_apellido','correo','celular','foto','sexo']

class CuidadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cuidador
        fields = ['rut_cuidador','nombre','p_apellido','s_apellido','fNacimiento','correo','celular','descripcion','tiempo_exp_lab','tarifa','foto','enlace_video','sexo']

class MenorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menor
        fields = ['rut_Menor','nombre','p_Apellido','s_Apellido','fNacimiento','sexo','rut_apoderado']