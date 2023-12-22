from django import forms
from .models import Inscrito, Institucion

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'telefono','fecha_inscripcion', 'institucion', 'hora_inscripcion', 'estado', 'observacion']

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']
