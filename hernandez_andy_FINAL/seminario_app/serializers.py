from rest_framework import serializers
from .models import Inscrito, Institucion
from django.shortcuts import render

def index(request):
    return render(request, '')

class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

