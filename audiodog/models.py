from django.db import models
import logging
logger = logging.getLogger(__name__)

# Create your models here.

from django.utils import timezone

class Cancion(models.Model):

    cancion = models.TextField(max_length=200)
    artista = models.TextField(max_length=100)
    duracion = models.TextField(max_length=5)
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE, null=False)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='cover', default='', null=False)
    archivo = models.FileField(default='', null=False, upload_to='audio/')

    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.cancion

class Usuario(models.Model):

    nombre = models.CharField(max_length=500, default='', null=False)

    alias = models.CharField(max_length=500, default='', null=False)
    contrasena = models.CharField(max_length=100, default='', null=False)

    rut = models.CharField(max_length=10)
    email = models.TextField(max_length=100)
    nacimiento_fecha = models.DateTimeField(default=timezone.now)
    telefonos = models.CharField(max_length=100)

    ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, default='', null=False)
    dispositivo = models.TextField(max_length=100)

    registro_fecha = models.DateTimeField(
            default=timezone.now)

    def crear(self):

        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.usuario

class Region(models.Model):

    region = models.CharField(max_length=100)
    registro_fecha = models.DateTimeField(default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return str(self.region)

class Ciudad(models.Model):

    ciudad = models.TextField(max_length=100)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    registro_fecha = models.DateTimeField(default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return str(self.ciudad)

class Pais(models.Model):

    pais = models.CharField(max_length=100)
    gentilicio = models.TextField(max_length=100)
    registro_fecha = models.DateTimeField(default=timezone.now)

    def crear(self):
        self.registro_fecha = timezone.now()
        self.save()

    def __str__(self):
        return self.pais

def file_get_contents(filename, use_include_path = 0, context = None, offset = -1, maxlen = -1):
    if (filename.find('://') > 0):
        ret = urllib2.urlopen(filename).read()
        if (offset > 0):
            ret = ret[offset:]
        if (maxlen > 0):
            ret = ret[:maxlen]
        return ret
    else:
        fp = open(filename,'rb')
        try:
            if (offset > 0):
                fp.seek(offset)
            ret = fp.read(maxlen)
            return ret
        finally:
            fp.close( )
