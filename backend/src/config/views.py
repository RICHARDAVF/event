from django.shortcuts import render
from rest_framework import viewsets
from .models import Config
from .serializer import ConfigSerializer

# Create your views here.
class ConfigView(viewsets.ModelViewSet):
    serializer_class = ConfigSerializer
    queryset = Config.objects.all()