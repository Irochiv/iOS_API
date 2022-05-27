from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'categoria'


class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    pedido_estatus = models.IntegerField()
    usuarios_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProducto(models.Model):
    pedido_pedido = models.OneToOneField(Pedido, models.DO_NOTHING, primary_key=True)
    producto_producto = models.ForeignKey('Producto', models.DO_NOTHING)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_producto'
        unique_together = (('pedido_pedido', 'producto_producto'),)


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    producto_nombre = models.CharField(max_length=45)
    producto_descripcion = models.CharField(max_length=1000)
    producto_precio = models.FloatField()
    producto_imagen = models.CharField(max_length=1000)
    categoria_categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'producto'


class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    usuario_nombre = models.CharField(max_length=100)
    usuario_correo = models.CharField(max_length=100)
    usuario_password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'usuarios'
