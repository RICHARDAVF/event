from rest_framework import routers
from .views import ClienteView, ProductoView, UserView,UsuarioView
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'client',ClienteView)
router.register(r'product',ProductoView)
router.register(r'usuarios',UsuarioView)
urlpatterns = [
    path('',include(router.urls)),
    path('client/login/<str:ruc>/<str:usuario>/<str:password>/', UserView.as_view()),
    
    
]