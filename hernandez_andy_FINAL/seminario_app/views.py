from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from seminario_app.models import Inscrito, Institucion
from seminario_app.forms import InscritoForm, InstitucionForm
from .serializers import InscritoSerializer, InstitucionSerializer
from django.urls import reverse

# Vista para la página principal
class IndexView(ListView):
    template_name = 'index.html'
    model = Inscrito
    context_object_name = 'inscritos'

# Vista para el listado de inscritos desde la interfaz
class InscritoListView(ListView):
    model = Inscrito
    template_name = 'inscrito_list_ui.html'
    context_object_name = 'inscritos'

# Vista para el formulario de ingreso de participantes
class InscritoCreateView(CreateView):
    model = Inscrito
    form_class = InscritoForm
    template_name = 'inscrito_form.html'
    
    def get_success_url(self):
        return reverse('inscrito_list_ui')

# Vista para el formulario de ingreso de instituciones
class InstitucionCreateView(CreateView):
    model = Institucion
    form_class = InstitucionForm
    template_name = 'institucion_form.html'
    
    def get_success_url(self):
        return reverse('api_institucion_list')

# Vista para la API de datos del autor
class AutorAPI(APIView):
    def get(self, request):
        autor_data = {
            'nombre': 'Andy Hernandez Villanueva',
            'rut': '20.139.177-6',
            'fecha': '22/12/2023',
            'asignatura': 'Programacion Backend',
            'seccion': 'IEI-170-N4'
        }
        return Response(autor_data)

# Vista para la API de participantes (Class Based View)
class InscritoListAPIView(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para la API de instituciones (Class Based View)
class InstitucionListAPIView(APIView):
    def get(self, request):
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para la API de instituciones (Function Based View)
@api_view(['GET', 'POST'])
def institucion_list_api(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista para mostrar detalles de un participante (Function Based View)
@api_view(['GET', 'PUT', 'DELETE'])
def inscrito_detalle(request, id):
    inscrito = get_object_or_404(Inscrito, id=id)

    if request.method == 'GET':
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vista para mostrar detalles de una institución (Function Based View)
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    institucion = get_object_or_404(Institucion, id=id)

    if request.method == 'GET':
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
