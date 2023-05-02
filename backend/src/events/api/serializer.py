from rest_framework import serializers
from ..models import ClienteUser, Productos
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteUser
        fields = ('id','ruc','usuario','password')
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
