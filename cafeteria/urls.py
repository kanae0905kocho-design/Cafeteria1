from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r"usuarios", UsuarioViewSets)
router.register(r"cafeteria", CafeteriaViewSets)
router.register(r"categoria", CategoriaViewSets)
router.register(r"roles", RolesViewSets)
router.register(r"productos", ProductoViewSets)
router.register(r"pedidos", PedidoViewSets)
router.register(r"pagos", PagoViewSets)
router.register(r"detalles-pedido", DetallePedidoViewSets)

urlpatterns = [
    path("api/", include(router.urls)),
]