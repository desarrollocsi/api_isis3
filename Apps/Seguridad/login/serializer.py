from rest_framework import serializers
from Apps.Seguridad.account.models  import User
from django.contrib.auth import authenticate
from ..menus.serializer import RolsSerializer

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    # roles = RolsSerializer(source="id_rol")
    # EspecialidadesSerializer(source="pr_servicio")
    class Meta:
        model = User
        fields = ('id', 'username', 'email','is_superuser','id_rol')

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("El usuario o la contraseña son invalidos")