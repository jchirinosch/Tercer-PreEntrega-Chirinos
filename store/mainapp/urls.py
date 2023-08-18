from django.urls import path, include
from .views import *

urlpatterns = [
        path('', home, name='home' ),
        path('guitarras/', guitarras, name='guitarras' ),
        path('bajos/', bajos, name='bajos' ),
        path('percusion/', percusion, name='percusion' ),
        path('sucursales/', sucursales, name='sucursales' ),

        path('guitarrasForm/', guitarrasform, name='guitarrasForm' ),
        path('bajosForm/', bajosform, name='bajosForm' ),
        path('percusionForm/', percusionform, name='percusionForm' ),

        path('buscarSucursal/', buscarSucursal, name = "buscarSucursal"),
        path('buscar2/', buscar2, name = "buscar2"),
]