from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre + " " + self.apellido

class Carrera(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()
    #jc = models.ForeignKey(Docente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre




