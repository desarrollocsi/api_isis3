from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label=("Oculto"),
        help_text=("Las contraseñas no se pueden visualizar "
                    "Si desea cambiar la contraseña use el siguiente enlace: "
                    "<a href=\"../password/\">Cambio de contraseña</a>."))

    class Meta:
        model = User
        fields = '__all__'


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username','email',)
    list_filter = ('username',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('id_rol','id_medico')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username','email','password1','password2')}),
    )
    search_fields = ('username','email')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)