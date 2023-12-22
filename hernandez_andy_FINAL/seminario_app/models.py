from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)  
    fecha_inscripcion = models.DateField()  
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField()  
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    observacion = models.TextField()

    def __str__(self):
        return self.nombre

