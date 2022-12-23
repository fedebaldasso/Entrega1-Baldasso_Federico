from django import forms

class JugadorForm(forms.Form):
    nombre= forms.CharField(label="Nombre Jugador", max_length=50)
    apellido= forms.CharField(label="Apellido Jugador", max_length=50)
    club= forms.CharField(label="Club Jugador", max_length=50)
    posicion= forms.CharField(label="Posición Jugador", max_length=50)
    edad=forms.IntegerField(label="Edad Jugador")
    fecha_nacimiento=forms.DateField(label="Fecha de Nacimiento")


class EquipoForm(forms.Form):
    nombre= forms.CharField(label="Nombre Equipo", max_length=50)
    pais= forms.CharField(label="Pais Equipo", max_length=50)

class EstadioForm(forms.Form):
    nombre= forms.CharField(label="Nombre Estadio", max_length=50)
    club= forms.CharField(label="Club Estadio", max_length=50)
    ciudad= forms.CharField(label="Ciudad Estadio", max_length=50)
    pais= forms.CharField(label="Pais Estadio", max_length=50)
    