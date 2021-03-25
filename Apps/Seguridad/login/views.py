from django.shortcuts import render

from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
# from rest_framework.authtoken.models import Token

from Apps.Seguridad.menus.models import Menu,Rol
from Apps.Seguridad.menus.serializer import Menuserializer,RolsSerializer


from knox.models import AuthToken
from rest_framework import generics # Vistas Genericas
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
        print(user)       
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
        # data = {
        #     "Usuario": UserSerializer(user,context = self.get_serializer_context()).data["username"],
        #     "Token" : AuthToken.objects.create(user)[1]
        # }
        return Response(data)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.AuthToken.delete()
        return Response(status=status.HTTP_200_OK)
# class LogoutAPI(generics.GenericAPIView):
    # user = request.user
    # serializer = LogoutSerializer(data=request.data,context={'request': request},)
    # serializer.is_valid(raise_exception=True)
    # data = serializer.validated_data
    # if should_authenticate_session():
    #     auth.logout(request)
    # if should_retrieve_token() and data['revoke_token']:
    #     auth_token_manager_cls = registration_settings.AUTH_TOKEN_MANAGER_CLASS
    #     auth_token_manager = auth_token_manager_cls()  # noqa: E501 type: rest_registration.auth_token_managers.AbstractAuthTokenManager
    #     auth_token_manager.revoke_token(user)

    # return get_ok_response(_("Logout successful"))
    # return Response({"Data" : "Logout"})





# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response("Usuario no registrado")
    
#     valid = check_password(password,user.password)
#     if not valid:
#         return Response("Contraseña incorrecta")
#     token, _ = Token.objects.get_or_create(user=user)

#     menus = Menus.objects.all().order_by('nivel','id')
#     serializer = Menuserializer(menus, many=True)
#     return Response({'menu':serializer.data,'token':token.key})

# @api_view(['POST'])
# def Logout(request):
#     user = request.user
#     serializer = LogoutSerializer(data=request.data,context={'request': request},)
#     serializer.is_valid(raise_exception=True)
#     data = serializer.validated_data
#     if should_authenticate_session():
#         auth.logout(request)
#     if should_retrieve_token() and data['revoke_token']:
#         auth_token_manager_cls = registration_settings.AUTH_TOKEN_MANAGER_CLASS
#         auth_token_manager = auth_token_manager_cls()  # noqa: E501 type: rest_registration.auth_token_managers.AbstractAuthTokenManager
#         auth_token_manager.revoke_token(user)

#     return get_ok_response(_("Logout successful"))