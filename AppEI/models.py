from django.db import models

# Create your models here.


class Jugador(models.Model):
    nombre= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    apellido=models.CharField(max_length=50)
    posicion=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    edad=models.IntegerField() #lo defino como un entero de base de datos
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return f"{self.nombre} - {str(self.apellido)}"

class Equipo(models.Model):
    nombre= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    pais=models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.nombre} - {str(self.pais)}"    

class Estadio(models.Model):
    nombre= models.CharField(max_length=50) #lo defino como un caracter de base de datos
    club= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=50)
    pais=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {str(self.ciudad)}"
