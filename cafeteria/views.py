from rest_framework import viewsets
from .models import * 
from .seriaizers import *

class CafeteriaViewSets(viewsets.ModelViewSet):
    queryset = Cafeteria.objects.all()
    serializer_class = CafeteriaSerializer


class CategoriaViewSets(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class RolesViewSets(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer


class UsuarioViewSets(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer


class PedidoViewSets(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class DetallePedidoViewSets(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoViewSets(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer