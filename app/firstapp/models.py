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
    pedido_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING)
    pedido_estatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido-producto'


class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    producto_descripcion = models.CharField(max_length=1000)
    producto_precio = models.FloatField()
    producto_imagen = models.CharField(max_length=1000)
    producto_categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

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
