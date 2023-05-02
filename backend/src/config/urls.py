from rest_framework import routers
from .views import  ConfigView
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'config',ConfigView)

urlpatterns = [
    path('',include(router.urls)),
    
]