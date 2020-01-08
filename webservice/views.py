from django.shortcuts import render

# Create your views here.
from webservice.serializers import operacion_serializer,  operacion2_serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from webservice.models import operacion,  operacion_vol
from .tasks import servicio_interruptor, servicio_volumen,  servicio_mudo,  servicio_interruptor_T

@csrf_exempt
def interruptor(request):
    
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer = operacion_serializer(data=data)
        if serializer.is_valid():
            datos=serializer.data
            comand=datos.get('comando')
            
            respuesta=servicio_interruptor.delay(comand)
            
            
            base=operacion.objects.create(comando=comand)
            serializer_comando=operacion_serializer(base)
            return JsonResponse(serializer_comando.data, status=201)
            
@csrf_exempt
def interruptor_T(request):
    
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer = operacion_serializer(data=data)
        if serializer.is_valid():
            datos=serializer.data
            comand=datos.get('comando')
            
            respuesta=servicio_interruptor_T.delay(comand)
            
            
            base=operacion.objects.create(comando=comand)
            serializer_comando=operacion_serializer(base)
            return JsonResponse(serializer_comando.data, status=201)

@csrf_exempt
def vol(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer = operacion2_serializer(data=data)
        if serializer.is_valid():
            datos=serializer.data
            comand=datos.get('comando')
            
            respuesta=servicio_volumen.delay(comand)
            
            base=operacion_vol.objects.create(comando=comand)
            serializer_comando=operacion2_serializer(base)
            return JsonResponse(serializer_comando.data, status=201)

@csrf_exempt       
def mudo(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        serializer = operacion_serializer(data=data)
        if serializer.is_valid():
            datos=serializer.data
            comand=datos.get('comando')
            
            respuesta=servicio_mudo.delay(comand)
            
            
            base=operacion.objects.create(comando=comand)
            serializer_comando=operacion_serializer(base)
            return JsonResponse(serializer_comando.data, status=201)
            
            
            
