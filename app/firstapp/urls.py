from django.urls import path

from . import views

urlpatterns = [
    path('',views.vista, name='vista'),
    path('login',views.login ,name='login'),
    path('register',views.register, name='register'),
    path('categoria',views.categoria, name='categoria'),
    path('categoria/<int:idCategoria>',views.productos,name='productos'),
    path('producto/<int:idProducto>',views.productosDetalles,name='detalles'),
    path('nuevopedido',views.pedidoNuevo,name='pedidonuevo'),
    path('pedido',views.pedido,name='pedido'),
]
