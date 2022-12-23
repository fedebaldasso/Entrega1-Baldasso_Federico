from django.shortcuts import render
from .models import Jugador, Equipo, Estadio
from django.http import HttpResponse
from AppEI.forms import JugadorForm, EquipoForm, EstadioForm

# Create your views here.

def inicio(request):
    return render (request, "AppEI/inicio.html")

def jugadorFormulario(request):  # Creación de formulario
    if request.method=="POST":
        form= JugadorForm(request.POST) #por POST el formulario viene lleno
        
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            posicion=informacion["posicion"]  
            club=informacion["club"] 
            edad=informacion["edad"] 
            fecha_nacimiento=informacion["fecha_nacimiento"]
            jugador= Jugador(nombre=nombre, apellido=apellido, posicion=posicion, club=club, edad=edad, fecha_nacimiento=fecha_nacimiento)
            jugador.save()
            jugadores=Jugador.objects.all()
            return render (request, "AppEI/leerJugadores.html", {"jugadores": jugadores, "mensaje": "Jugador guardado correctamente"})
        else:
            return render (request, "AppEI/jugadorFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else: #sino viene por GET y el formulario viene vacío
        formulario= JugadorForm()
        return render (request, "AppEI/jugadorFormulario.html", {"form": formulario})


def equipoFormulario(request):  # Creación de formulario
    if request.method=="POST":
        form= EquipoForm(request.POST) #por POST el formulario viene lleno
       
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            
            nombre=informacion["nombre"]
            pais=informacion["pais"]            
            equipo= Equipo(nombre=nombre, pais=pais)
            equipo.save()
            equipos=Equipo.objects.all()
            return render (request, "AppEI/leerEquipos.html", {"equipos": equipos, "mensaje": "Equipo guardado correctamente"})
        else:
            return render (request, "AppEI/equipoFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else: #sino viene por GET y el formulario viene vacío
        formulario= EquipoForm()
        return render (request, "AppEI/equipoFormulario.html", {"form": formulario})


def estadioFormulario(request):  # Creación de formulario
    if request.method=="POST":
        form= EstadioForm(request.POST) #por POST el formulario viene lleno
        
        if form.is_valid():
            informacion=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            
            nombre=informacion["nombre"]
            club=informacion["club"]
            ciudad=informacion["ciudad"]
            pais=informacion["pais"]
            estadio= Estadio(nombre=nombre, club=club, ciudad=ciudad, pais=pais)
            estadio.save()
            estadios=Estadio.objects.all()
            return render (request, "AppEI/leerEstadios.html", {"estadios": estadios, "mensaje": "Estadio guardado correctamente"})
        else:
            return render (request, "AppEI/estadioFormulario.html", {"form": form, "mensaje": "Información no válida"})

    else: #sino viene por GET y el formulario viene vacío
        formulario= EstadioForm()
        return render (request, "AppEI/estadioFormulario.html", {"form": formulario})


def busquedaJugador(request):
    return render(request, "AppEI/busquedaJugador.html")

def buscar(request):
    
    apellido=request.GET["apellido"]
    if apellido!="":
        jugadores= Jugador.objects.filter(apellido__icontains=apellido) #Busca los jugadores que corresponden al apellido que mandé por GET
        return render (request, "AppEI/resultadosBusqueda.html", {"jugadores": jugadores})
    else:
        return render (request, "AppEI/busquedaJugador.html", {"mensaje": "Ingresa un jugador a buscar!"})


def leerJugadores(request):
    jugadores=Jugador.objects.all()
    return render (request, "AppEI/leerJugadores.html", {"jugadores": jugadores})

def eliminarJugador(request, id):
    jugador=Jugador.objects.get(id=id)
    jugador.delete()
    jugadores=Jugador.objects.all()
    return render (request, "AppEI/leerJugadores.html", {"jugadores": jugadores, "mensaje": "Jugador eliminado correctamente"})

def editarJugador(request, id):
    jugador=Jugador.objects.get(id=id)
    if request.method=="POST":
        form= JugadorForm(request.POST) #por POST el formulario viene lleno        
        if form.is_valid():
            info=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            jugador.nombre=info["nombre"]
            jugador.apellido=info["apellido"]
            jugador.posicion=info["posicion"]
            jugador.club=info["club"]
            jugador.edad=info["edad"]
            jugador.fecha_nacimiento=info["fecha_nacimiento"]               
            jugador.save()
            jugadores=Jugador.objects.all()
            return render (request, "AppEI/leerJugadores.html", {"jugadores": jugadores, "mensaje": "Jugador editado correctamente"})
        pass
    else:
        formulario=JugadorForm(initial={"nombre":jugador.nombre, "apellido":jugador.apellido, "posicion": jugador.posicion, "club": jugador.club, "edad": jugador.edad, "fecha_nacimiento": jugador.fecha_nacimiento})
        return render (request, "AppEI/editarJugador.html", {"form": formulario, "jugador": jugador})


def leerEquipos(request):
    equipos=Equipo.objects.all()
    return render (request, "AppEI/leerEquipos.html", {"equipos": equipos})

def eliminarEquipo(request, id):
    equipo=Equipo.objects.get(id=id)
    equipo.delete()
    equipos=Equipo.objects.all()
    return render (request, "AppEI/leerEquipos.html", {"equipos": equipos, "mensaje": "Equipo eliminado correctamente"})

def editarEquipo(request, id):
    equipo=Equipo.objects.get(id=id)
    if request.method=="POST":
        form= EquipoForm(request.POST) #por POST el formulario viene lleno        
        if form.is_valid():
            info=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            equipo.nombre=info["nombre"]
            equipo.pais=info["pais"]            
            equipo.save()
            equipos=Equipo.objects.all()
            return render (request, "AppEI/leerEquipos.html", {"equipos": equipos, "mensaje": "Equipo editado correctamente"})
        pass
    else:
        formulario=EquipoForm(initial={"nombre":equipo.nombre, "pais":equipo.pais})
        return render (request, "AppEI/editarEquipo.html", {"form": formulario, "equipo": equipo})


def leerEstadios(request):
    estadios=Estadio.objects.all()
    return render (request, "AppEI/leerEstadios.html", {"estadios": estadios})

def eliminarEstadio(request, id):
    estadio=Estadio.objects.get(id=id)
    estadio.delete()
    estadios=Estadio.objects.all()
    return render (request, "AppEI/leerEstadios.html", {"estadios": estadios, "mensaje": "Estadio eliminado correctamente"})

def editarEstadio(request, id):
    estadio=Estadio.objects.get(id=id)
    if request.method=="POST":
        form= EstadioForm(request.POST) #por POST el formulario viene lleno        
        if form.is_valid():
            info=form.cleaned_data #convierte la info en modo formulario a un diccionario más facil de leer
            estadio.nombre=info["nombre"]
            estadio.club=info["club"]
            estadio.ciudad=info["ciudad"]
            estadio.pais=info["pais"]     
            estadio.save()
            estadios=Estadio.objects.all()
            return render (request, "AppEI/leerEstadios.html", {"estadios": estadios, "mensaje": "Estadio editado correctamente"})
        pass
    else:
        formulario=EstadioForm(initial={"nombre":estadio.nombre, "club":estadio.club, "ciudad": estadio.ciudad, "pais": estadio.pais})
        return render (request, "AppEI/editarEstadio.html", {"form": formulario, "estadio": estadio})
