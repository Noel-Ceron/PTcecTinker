# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from webservice.models import operacion, operacion_vol

class operacion_serializer(ModelSerializer):
    class Meta:
        model=operacion
        fields=['comando',]

class operacion2_serializer(ModelSerializer):
    class Meta:
        model=operacion_vol
        fields=['comando',]
