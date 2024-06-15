from flask import Blueprint, jsonify, request
from servicio.productos import *
from flasgger import swag_from

producto_blueprint = Blueprint('producto', __name__)

################################################################################
#                           PRODUCTOS                                           #
################################################################################

@producto_blueprint.route('/productos', methods=['GET'])
@swag_from({
    'tags': ['PRODUCTOS'],
    'summary':'Obtener todos los productos existentes',
    'description':'Obtener todos los productos existentes',
    'responses': {
        200: {
            'description': 'Una lista de produtos productos',
            'examples': {
                'application/json': [
                    {'id': 1, 'nombre': 'Producto 1', 'stock': '10', 'precio': '10.5', 'id_proveedor':1},
                    {'id': 1, 'nombre': 'Producto 2', 'stock': '15', 'precio': '5.75', 'id_proveedor':2},
                ]
            }
        }
    }
})
def get_productos():
    productos = ProductoService.get_all_productos()
    return jsonify([producto.as_dict() for producto in productos])



@producto_blueprint.route('/nuevoProducto', methods=['POST'])
@swag_from({
    'tags': ['PRODUCTOS'],
    'summary':'Creacion de un nuevo producto',
    'description':'Creacion de un nuevo producto',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string'},
                    'stock': {'type': 'int'},
                    'precio': {'type': 'float'},
                    'id_proveedor': {'type': 'int'}}
                }
            }
    ],
    'responses': {
        201: {
            'description': 'Creación Exitosa',
            'examples': {
                    'application/json': {'id': 1, 'nombre': 'Producto 2', 'stock': '15', 'precio': '5.75', 'id_proveedor':2},
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def add_producto():
    data = request.get_json()
    producto = ProductoService.add_producto(data)
    return jsonify(producto.as_dict()), 201

@producto_blueprint.route('/eliminarProducto', methods=['POST'])
@swag_from({
    'tags': ['PRODUCTOS'],
    'summary':'Eliminar un producto',
    'description':'Eliminar un producto',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Eliminación Exitosa',
            'examples': {
                'application/json': {'id': 1}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def delete_producto():
    data = request.get_json()
    producto = ProductoService.delete_producto(data)
    return jsonify(producto.as_dict()), 200

@producto_blueprint.route('/obtProducto', methods=['POST'])
@swag_from({
    'tags':['PRODUCTOS'],
    'summary':'Obtener Producto Especifico Por ID',
    'description':'Obtener Producto Especifico Por ID',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Busqueda Exitosa',
            'examples': {
                   'application/json': {'id': 1, 'nombre': 'Producto 2', 'stock': '15', 'precio': '5.75', 'id_proveedor':2},
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def obtener_producto():
    data = request.get_json()
    producto = ProductoService.get_producto_by_id(data)
    return jsonify(producto.as_dict()), 200


################################################################################
#                           PROVEEDORES                                        #
################################################################################
@producto_blueprint.route('/obtProveedores', methods=['GET'])
@swag_from({
    'tags':['PROVEEDORES'],
    'summary':'Obtener una lista de todos los proveedores',
    'description':'Obtener una lista de todos los proveedores',
    'responses': {
        200: {
            'description': 'Una lista de proveedores',
            'examples': {
                'application/json': [
                    {'id': 1, 'nombre': 'Proveedor 1'},
                    {'id': 2, 'nombre': 'Proveedor 2'}
                ]
            }
        }
    }
})
def get_Proveedor():
    proveedores = ProductoService.get_Proveedores()
    return jsonify([proveedor.as_dict() for proveedor in proveedores])


@producto_blueprint.route('/nuevoProveedor', methods=['POST'])
@swag_from({
    'tags':['PROVEEDORES'],
    'summary':'Creacion de un nuevo proveedor',
    'description':'Creacion de un nuevo proveedor',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string'},
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Creación Exitosa',
            'examples': {
                    'application/json': {'id': 1, 'nombre': 'Proveedor 1'},
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def add_proveedor():
    data = request.get_json()
    proveedor = ProductoService.add_Proveedor(data)
    return jsonify(proveedor.as_dict()), 201

@producto_blueprint.route('/eliminarProveedor', methods=['POST'])
@swag_from({
    'tags':['PROVEEDORES'],
    'summary':'Eliminar un proveedor',
    'description':'Eliminar un proveedor',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Eliminación Exitosa',
            'examples': {
                'application/json': {'id': 1}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def delete_proveedores():
    data = request.get_json()
    proveedores = ProductoService.delete_proveedores(data)
    return jsonify(proveedores.as_dict()), 200