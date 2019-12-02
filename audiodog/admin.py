from django.contrib import admin

# Register your models here.

from .models import Cancion
from .models import Pais
from .models import Region
from .models import Ciudad

admin.site.register(Cancion)
admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Ciudad)
