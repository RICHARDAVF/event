from rest_framework import viewsets,generics
from ..models import ClienteUser, Productos, Usuarios
from .serializer import ClienteSerializer, ProductoSerializer, UsuarioSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework import status
class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = ClienteUser.objects.all()


class UserView(generics.GenericAPIView):
    serializer_class = ClienteSerializer

    def get(self, request, *args, **kwargs):
        ruc = kwargs['ruc']
        usuario = kwargs['usuario']
        password = kwargs['password']

        try:
            user = ClienteUser.objects.get(ruc=ruc, usuario=usuario)

            if check_password(password, user.password):
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response([], status=status.HTTP_401_UNAUTHORIZED)
        except ClienteUser.DoesNotExist:
            return Response([], status=status.HTTP_404_NOT_FOUND)
        


class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Productos.objects.all()
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuarios.objects.all()