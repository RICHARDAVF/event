from rest_framework import serializers
from ..models import ClienteUser, Productos, Usuarios
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteUser
        fields = ('id','ruc','usuario','password')
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'