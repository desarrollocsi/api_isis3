from django.shortcuts import render

from Apps.Seguridad.menus.models import Menu,Rol
from Apps.Seguridad.menus.serializer import Menuserializer,RolsSerializer

from knox.models import AuthToken
from rest_framework import generics, status # Vistas Genericas
from rest_framework.response import Response
from Apps.Seguridad.account.models  import User
from .serializer import UserSerializer,LoginUserSerializer
from rest_framework.views import APIView
# Create your views here.

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if UserSerializer(user,context = self.get_serializer_context()).data["is_superuser"]:
            Objmenus        = Menu.objects.all().order_by('nivel','nombre')
            serializermenu  = Menuserializer(Objmenus, many=True)
            rol = [{ "nombre" : "SUPERADMIN",
            "menu": serializermenu.data}]
        else:
            idRol           = UserSerializer(user,context = self.get_serializer_context()).data["id_rol"]
            ObjRol          = Rol.objects.filter(id = idRol)
            serializerol    = RolsSerializer(ObjRol,many=True)
            rol = serializerol.data
        data = {
            "User":  UserSerializer(user,context = self.get_serializer_context()).data,
            "Rol":rol,
            "Token" : AuthToken.objects.create(user)[1]
        }
        return Response(data)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.AuthToken.delete()
        return Response(status=status.HTTP_200_OK)