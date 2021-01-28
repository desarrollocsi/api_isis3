from django.contrib import admin

# Register your models here.
from .models import options,formularioc,formulariod

# Register your models here.
# admin.site.register(elementos)
admin.site.register(formularioc)
admin.site.register(formulariod)
admin.site.register(options)