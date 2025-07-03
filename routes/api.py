from flask import Blueprint, jsonify, request
from controllers.ProductoController import (
    mostrar_productos, obtener_producto, crear_producto, actualizar_producto,
    eliminar_producto
)

api = Blueprint('api',__name__)

@api.route('/productos', methods=['GET'])
def get_productos():
    productos = mostrar_productos()
    return jsonify(productos),200

@api.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    try:
        producto = obtener_producto(id)
        return jsonify(producto),200
    except:
        return jsonify({'error':'Producto no encontrado'}), 404

@api.route('/productos', methods=['POST'])
def post_producto():
    try:
        producto = crear_producto()
        return jsonify(producto), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api.route('/productos/<int:id>', methods=['PATCH'])
def patch_producto(id):
    producto = actualizar_producto(id)
    if isinstance(producto, tuple):  # si es (json, 404)
        return producto
    return jsonify(producto), 200

@api.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    try:
        producto = eliminar_producto(id)
        return jsonify(producto), 200
    except:
        return jsonify({'error': 'Producto no encontrado'})