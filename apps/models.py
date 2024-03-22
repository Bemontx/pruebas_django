from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    edad = models.SmallIntegerField()
    fecha_ingreso = models.DateField()
    email = models.CharField(max_length = 50)

    def __str__(self) -> str:
        texto = "{0} ({1})"
        # return self.nombre
        return texto.format(self.nombre, self.email)