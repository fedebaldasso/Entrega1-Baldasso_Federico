from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="inicio"),

    path('jugadorFormulario/', jugadorFormulario, name="jugadorFormulario"),
    path('equipoFormulario/', equipoFormulario, name="equipoFormulario"),
    path('estadioFormulario/', estadioFormulario, name="estadioFormulario"),

    path('busquedaJugador/', busquedaJugador, name="busquedaJugador"),
    path('buscar/', buscar, name="buscar"),

    path('leerJugadores/', leerJugadores, name="leerJugadores"),
    path('eliminarJugador/<id>', eliminarJugador, name="eliminarJugador"),
    path('editarJugador/<id>', editarJugador, name="editarJugador"),

    path('leerEquipos/', leerEquipos, name="leerEquipos"),
    path('eliminarEquipo/<id>', eliminarEquipo, name="eliminarEquipo"),
    path('editarEquipo/<id>', editarEquipo, name="editarEquipo"),

    path('leerEstadios/', leerEstadios, name="leerEstadios"),
    path('eliminarEstadio/<id>', eliminarEstadio, name="eliminarEstadio"),
    path('editarEstadio/<id>', editarEstadio, name="editarEstadio"),
    

]