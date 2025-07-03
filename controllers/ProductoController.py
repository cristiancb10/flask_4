from models.Producto import Producto
from flask import Flask, request


def mostrar_productos():
    productos = Producto.select().where(Producto.eliminado == False).dicts()
    return list(productos)

def obtener_producto(id):
    producto = Producto.get_or_none(Producto.id == id)
    if producto:       
        return{
            'id': producto.id,
            'nombre': producto.nombre,
            'costo': producto.costo,
            'precio': producto.precio,
            'stock': producto.stock,
            'creado_en': producto.creado_en,
            'actualizado_en': producto.actualizado_en,
            'eliminado':producto.eliminado
        }
    return {'error': 'Producto no encontrado'}, 404

def crear_producto():
    datos = request.get_json()
    producto = Producto.create(
        nombre = datos['nombre'],
        costo = datos['costo'],
        precio = datos['precio'],
        stock = datos['stock']
    )
    return{
        'id': producto.id,
        'nombre': producto.nombre,
        'costo': producto.costo,
        'precio': producto.precio,
        'stock': producto.stock,
        'creado_en': producto.creado_en,
        'actualizado_en': producto.actualizado_en,
        'eliminado':producto.eliminado
    }
    
def actualizar_producto(id):
    producto = Producto.get_or_none(Producto.id == id)
    if not producto:
        return {'error': 'Producto no encontrado'}, 404

    datos = request.get_json()

    producto.nombre = datos.get('nombre', producto.nombre)
    producto.costo = datos.get('costo', producto.costo)
    producto.precio = datos.get('precio', producto.precio)
    producto.stock = datos.get('stock', producto.stock)
    producto.eliminado = datos.get('eliminado', producto.eliminado)
    
    producto.save()  
    
    return {
        'id': producto.id,
        'nombre': producto.nombre,
        'costo': producto.costo,
        'precio': producto.precio,
        'stock': producto.stock,
        'creado_en': producto.creado_en,
        'actualizado_en': producto.actualizado_en,
        'eliminado': producto.eliminado
    }

def eliminar_producto(id):
    producto = Producto.get_or_none(Producto.id == id)
    if not producto:
        return {'error': 'Producto no encontrado'}, 404

    producto.eliminado = True
    producto.save()
    
    return{
        'id': producto.id,
        'nombre': producto.nombre,
        'costo': producto.costo,
        'precio': producto.precio,
        'stock': producto.stock,
        'creado_en': producto.creado_en,
        'actualizado_en': producto.actualizado_en,
        'eliminado': producto.eliminado
    }