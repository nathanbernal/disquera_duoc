
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import render
from .models import Cancion, Region, Ciudad, Usuario, Pais
from django.http import JsonResponse
import logging
from .forms import UsuarioForm
from django.http import HttpResponseRedirect

logger = logging.getLogger(__name__)


def cancion_list(request):
    canciones = Cancion.objects.filter(registro_fecha__lte=timezone.now()).order_by('registro_fecha')
    usuarios = Usuario.objects.all()
    return render(request, 'audiodog/cancion_list.html', {'canciones' : canciones, 'usuarios' : usuarios})

def usuario_registro(request):

    regiones = Region.objects.all()
    return render(request, 'audiodog/usuario_registro.html', {'regiones': regiones })

def usuario_guardar(request):

    dispositivo = [
        (1, 'computador'),
        (2, 'Teléfono móvil'),
        (3, 'Tablet'),
        (4, 'Smart TV'),
    ]

    logger.error('GUARDANDO USUARIO  '+request.POST["nombre"])

    usuario = Usuario()
    usuario.nombre = request.POST["nombre"]
    usuario.rut = request.POST["rut"]
    usuario.email = request.POST["correo"]
    usuario.nacimiento_fecha = request.POST["fechanacimento"]
    usuario.telefonos = request.POST["telefono"]

    usuario.ciudad = Ciudad.objects.get(id=request.POST["ciudad"])

    dispositivoSel='';

    for d in dispositivo:

        logger.error('DD:'+str(d))

        if request.POST["ciudad"] != '':
            dispositivoSel.join("&".join(str(d)))

    usuario.dispositivo = dispositivoSel

    usuario.save()

    return HttpResponseRedirect('/')

def usuario_eliminar(request):

    logger.error('ELIMINANDO USUARIO  '+request.GET["usuario_id"])

    usuario_id=request.GET["usuario_id"]
    usuario = Usuario.objects.filter(id=usuario_id)
    usuario.delete()

    return JsonResponse({"status":"success"})

def ciudad_get(request):

    logger.error('RECUPERANDO CIUDADES ')

    region_id = request.GET['region_id']
    logger.error('REGIÓN IDENTIFICADA COMO  '+region_id)

    ciudades = Ciudad.objects.filter(region__exact=region_id).order_by('ciudad')
    c = {}

    for ciudad in ciudades:
        c[ciudad.id]=ciudad.ciudad

    return JsonResponse(c)

def cancion_subir(request):

    paises = Pais.objects.all()
    return render(request, 'audiodog/cancion_subir.html', { 'paises' : paises })

def cancion_guardar(request):

    cancion = Cancion()

    cancion.cancion = request.POST["cancion"]
    cancion.artista = request.POST["artista"]
    cancion.duracion = request.POST["duracion"]
    cancion.pais = Pais.objects.get(id=request.POST["pais"])
    cancion.imagen = request.FILES["caratula"]
    cancion.archivo = request.FILES["audio"]

    cancion.save();

    return HttpResponseRedirect('/')
