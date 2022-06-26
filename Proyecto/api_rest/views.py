from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Go_mon.models import Apoderado, Cuidador, Menor
from .serializers import ApoderadoSerializers, CuidadorSerializers, MenorSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#APODERADO
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_apoderados(request):
    if request.method == 'GET':
        apoderados = Apoderado.objects.all()
        serializer = ApoderadoSerializers(apoderados,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ApoderadoSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarApoderado(request,rut):
    try:
        a = Apoderado.objects.get(rut_apoderado = rut)
    except Apoderado.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ApoderadoSerializers(a)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ApoderadoSerializers(a, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        a.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#CUIDADOR
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_cuidadores(request):
    if request.method == 'GET':
        cuidadores = Cuidador.objects.all()
        serializer = CuidadorSerializers(cuidadores,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CuidadorSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def modEliminarCuidador(request,rut):
    try:
        c = Cuidador.objects.get(rut_cuidador = rut)
    except Cuidador.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CuidadorSerializers(c)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = CuidadorSerializers(c, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        c.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#MENOR

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listado_menores(request):
    if request.method == 'GET':
        menores = Menor.objects.all()
        serializer = MenorSerializers(menores,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenorSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_menor(request,rut):
    try:
        m = Menor.objects.get(rut_Menor = rut)
    except Menor.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MenorSerializers(m)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = MenorSerializers(m, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        m.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)