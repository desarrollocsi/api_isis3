from django.contrib import admin

# Register your models here.
from .models import Rol,Menu

# Register your models here.
# admin.site.register(elementos)
admin.site.register(Rol)
admin.site.register(Menu)
