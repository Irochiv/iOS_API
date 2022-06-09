# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from hashlib import new
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
from django.db import connection
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password


from .models import Categoria, Pedido, Producto, Usuarios, PedidoProducto

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'clase.html', {'title': "Bumblebee" })



def login(request):
    if request.method == 'POST':
        try: 
            json_object = json.loads(request.body)
        except KeyError as e:
            responseData ={}
            responseData['status_message'] = 'Invalid JSON'
            responseData['status_code'] = 'False'
            return JsonResponse(responseData, status=400)
        try:
            one_entry = Usuarios.objects.get(usuario_correo=json_object['correo'], usuario_password=json_object['password'])
        except:
            responseData ={}
            responseData['status_message'] = 'Desconectado'
            responseData['status_code'] = 'True'
            return JsonResponse(responseData, status=200)

        responseData = {}
        data = list(Usuarios.objects.filter(usuario_correo=json_object['correo'], usuario_password=json_object['password']).values())
        responseData['data']= data[0]  
        responseData['status_message'] = 'Conectado'
        responseData['status_code'] = 'True'
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)

def register(request):
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
            b = Usuarios(usuario_nombre=json_object['nombre'], usuario_correo = json_object['correo'], usuario_password = json_object['password'])
            b.save()
            responseData = {}
            responseData['status_message'] = 'Usuario creado'
            responseData['status_code'] = 'True'

            return JsonResponse(responseData, status=200)

        except KeyError as e:
            responseData ={}
            responseData['status_message'] = 'Invalid JSON'
            responseData['status_code'] = 'False'
            return JsonResponse(responseData, status=400)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)





def categoria(request):
    if request.method == 'GET':
        reponseData = {}
        reponseData['success'] = 'true'
        reponseData['data'] = list(Categoria.objects.all().values())
        return JsonResponse(reponseData, status=200)
    else:
        reponseData = {}
        reponseData['success'] = 'false'
        reponseData['message'] = 'Wrong Method'
        return JsonResponse(reponseData, status=400)

def productos(request, idCategoria):
    if request.method == 'GET':
        try: 
            one_entry = Categoria.objects.get(categoria_id = idCategoria)
        except:
            responseData ={}
            responseData['status_message'] = 'The id its not valid'
            responseData['status_code'] = 'False'
            return JsonResponse(responseData, status=400)

        responseData = {}
        
        data = list(Producto.objects.filter(categoria_categoria=idCategoria).values())
        responseData['data']= data  
        responseData['status_message'] = 'Conectado'
        responseData['status_code'] = 'True'
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)

def productosDetalles(request, idProducto):
    if request.method == 'GET':
        try: 
            one_entry = Producto.objects.get(producto_id=idProducto)
        except:
            responseData ={}
            responseData['status_message'] = 'The id its not valid'
            responseData['status_code'] = 'False'
            return JsonResponse(responseData, status=400)

        responseData = {}
        
        data = list(Producto.objects.filter(producto_id=idProducto).values())
        responseData['data']= data[0]  
        responseData['status_message'] = 'Conectado'
        responseData['status_code'] = 'True'
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)

def pedidoNuevo(request):
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
            user = Usuarios.objects.get(usuario_id = json_object['iduser'])
            b = Pedido(pedido_estatus = json_object['estatus'], usuarios_usuario = user)
            b.save()
            
            try:
                # for product in json_object['products']:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO pedido_producto (pedido_pedido_id, producto_producto_id, cantidad) values (%s,%s,%s)", [b.pedido_id, json_object['idproducto'], json_object['cantidad'] ]) 
                cursor.fetchall()
                cursor.close()
                # p = Producto.objects.get(producto_id = json_object['idproducto'])
                # pp = PedidoProducto(b,p,json_object['cantidad'])
                # pp.save()

            except KeyError as e:
                b.delete()
                responseData = {}
                responseData['status_message'] = e.text()
                responseData['status_code'] = 'False'
                return JsonResponse(responseData, status=400)

            responseData = {}
            responseData['pedido_id']= b.pedido_id
            responseData['status_message'] = 'Pedido Creado'
            responseData['status_code'] = 'True'

            return JsonResponse(responseData, status=200)

        except KeyError as e:
            responseData ={}
            responseData['status_message'] = 'Invalid JSON'
            responseData['status_code'] = 'False'
            return JsonResponse(responseData, status=400)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)

def pedidos(request,iduser):
    if request.method == 'GET':

        responseData = {}
        cursor = connection.cursor()
        cursor.execute("SELECT u.usuario_nombre, u.usuario_correo, p.pedido_estatus, c.categoria_nombre, pr.producto_nombre, pr.producto_descripcion, pr.producto_precio, pp.cantidad, p.pedido_id  FROM pedido p join pedido_producto pp on p.pedido_id = pp.pedido_pedido_id join producto pr on pp.producto_producto_id = pr.producto_id join usuarios u on p.usuarios_usuario_id = u.usuario_id join categoria c on c.categoria_id = pr.categoria_categoria_id where u.usuario_id = %s", [iduser]) 
        datos = cursor.fetchall()
        data = list()
        for d in datos:
            data.append({"Nombre": d[0], "Correo": d[1], "Estatus": d[2], "Categoria": d[3], "Modelo": d[4], "Descripcion": d[5], "Precio": d[6], "Cantidad": d[7], "Pedido_id":d[8]})
        responseData['data']= data  
        responseData['status_message'] = 'Conectado'
        responseData['status_code'] = 'True'
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)

def pedido(request,iduser,idpedido):
    if request.method == 'GET':
        try: 
            one_entry = Pedido.objects.get(pedido_id=idpedido)
        except KeyError as e:
            responseData ={}
            responseData['status_message'] = 'The id its not valid'
            responseData['status_code'] = 'False'
            return JsonResponse(responseData, status=400)

        responseData = {}
        
        cursor = connection.cursor()
        cursor.execute("SELECT u.usuario_nombre, u.usuario_correo, p.pedido_estatus, c.categoria_nombre, pr.producto_nombre, pr.producto_descripcion, pr.producto_precio, pp.cantidad, p.pedido_id  FROM pedido p join pedido_producto pp on p.pedido_id = pp.pedido_pedido_id join producto pr on pp.producto_producto_id = pr.producto_id join usuarios u on p.usuarios_usuario_id = u.usuario_id join categoria c on c.categoria_id = pr.categoria_categoria_id where u.usuario_id = %s and p.pedido_id = %s", [iduser, idpedido]) 
        datos = cursor.fetchall()
        data = list()
        for d in datos:
            data.append({"Nombre": d[0], "Correo": d[1], "Estatus": d[2], "Categoria": d[3], "Modelo": d[4], "Descripcion": d[5], "Precio": d[6], "Cantidad": d[7], "Pedido_id":d[8]})
        responseData['data']= data  
        responseData['status_message'] = 'Conectado'
        responseData['status_code'] = 'True'
        return JsonResponse(responseData, status=200)
    
    else:
        responseData ={}
        responseData['status_message'] = 'Wrong method'
        responseData['status_code'] = 'False'
        return JsonResponse(responseData, status=404)




# def dogs(request):
    
#     if request.method == 'GET':
#         reponseData = {}
#         reponseData['success'] = 'true'
#         reponseData['data'] = list(Dogs.objects.all().values())
#         return JsonResponse(reponseData, status=200)
#     else:
#         reponseData = {}
#         reponseData['success'] = 'false'
#         reponseData['message'] = 'Wrong Method'
#         return JsonResponse(reponseData, status=400)


# def dogsAdd(request):
    
#     if request.method == 'POST':
#         try:
#             reponseData = {}
#             json_object = json.loads(request.body)
#             newDog= Dogs(name=json_object['dog_name'], type_id=json_object['dog_type_id'], color=json_object['dog_color'], size=json_object['dog_size'])
#             newDog.save()
#             reponseData['success'] = 'true'
#             reponseData['message'] = 'Dog inserted'
#             return JsonResponse(reponseData, status=200) 
#         except ValueError as e:
#             reponseData = {}
#             reponseData['success'] = 'false'
#             reponseData['message'] = 'Invalid Json'
#             return JsonResponse(reponseData, status=400) 
        
#     else:
#         reponseData = {}
#         reponseData['success'] = 'false'
#         reponseData['message'] = 'Wrong Method'
#         return JsonResponse(reponseData, status=400)


# def dogsDelete(request):
    
#     if request.method == 'DELETE':
#         try:
#             reponseData = {}
#             json_object = json.loads(request.body)
#             reponseData['success'] = 'true'
#             reponseData['message'] = 'Valid Json'
#             return JsonResponse(reponseData, status=200) 
#         except ValueError as e:
#             reponseData = {}
#             reponseData['success'] = 'false'
#             reponseData['message'] = 'Invalid Json'
#             return JsonResponse(reponseData, status=400) 
        
#     else:
#         reponseData = {}
#         reponseData['success'] = 'false'
#         reponseData['message'] = 'Wrong Method'
#         return JsonResponse(reponseData, status=400)


# def types(request):
    
#     if request.method == 'GET':
#         reponseData = {}
#         reponseData['success'] = 'true'
#         reponseData['data'] = list(Types.objects.all().values())
#         return JsonResponse(reponseData, status=200)
#     else:
#         reponseData = {}
#         reponseData['success'] = 'false'
#         reponseData['message'] = 'Wrong Method'
#         return JsonResponse(reponseData, status=400)
    

