from flask import Blueprint, jsonify, request
from servicio.usuarios import *
from flasgger import swag_from

usuario_blueprint = Blueprint('usuario', __name__)

################################################################################
#                           USUARIOS                                           #
################################################################################

@usuario_blueprint.route('/usuarios', methods=['GET'])
@swag_from({
    'tags':['USUARIOS'],
    'summary':'Obtener todos los usuarios existentes',
    'description':'Obtener todos los usuarios existentes',
    'responses': {
        200: {
            'description': 'Una lista de usuarios',
            'examples': {
                'application/json': [
                    {'id': 1, 'nombre': 'Usuario 1', 'cedula': '1234567890', 'id_rol': 1},
                    {'id': 2, 'nombre': 'Usuario 2', 'cedula': '0987654321', 'id_rol': 2}
                ]
            }
        }
    }
})
def get_usuarios():
    usuarios = UsuarioService.get_all_usuarios()
    return jsonify([usuario.as_dict() for usuario in usuarios])



@usuario_blueprint.route('/nuevoUsuario', methods=['POST'])
@swag_from({
    'tags':['USUARIOS'],
    'summary':'Creacion de Nuevo Usuario',
    'description':'Creacion de Nuevo Usuario',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre': {'type': 'string'},
                    'cedula': {'type': 'string'},
                    'id_rol': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Creación Exitosa',
            'examples': {
                'application/json': {'id': 1, 'nombre': 'Andrew Rueda', 'cedula': '1722225461', 'id_rol': 2}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def add_usuario():
    data = request.get_json()
    usuario = UsuarioService.add_usuario(data)
    return jsonify(usuario.as_dict()), 201

@usuario_blueprint.route('/eliminarUsuario', methods=['POST'])
@swag_from({
    'tags':['USUARIOS'],
    'summary':'Eliminar Usuario por ID',
    'description':'Eliminar Usuario por ID',
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
def delete_usuario():
    data = request.get_json()
    usuario = UsuarioService.delete_usuario(data)
    return jsonify(usuario.as_dict()), 200

@usuario_blueprint.route('/obtUsuario', methods=['POST'])
@swag_from({
    'tags':['USUARIOS'],
    'summary':'Obtener Usuario Especifico Por ID',
    'description':'Obtener Usuario Especifico Por ID',
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
                'application/json': {'id': 1,'nombre':'Adrian Villacres','cedula':'085007269','id_rol':1}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def obtener_usuario():
    data = request.get_json()
    usuario = UsuarioService.get_usuario_by_id(data)
    return jsonify(usuario.as_dict()), 200


################################################################################
#                           ROLES                                              #
################################################################################
@usuario_blueprint.route('/obtRoles', methods=['GET'])
@swag_from({
    'tags':['ROLES'],
    'summary':'Obtener Todos los Roles Existentes',
    'description':'Obtener Todos los Roles Existentes',
    'responses': {
        200: {
            'description': 'Lista de roles obtenidos',
            'examples': {
                'application/json': [
                    {'id': 1, 'nombre': 'Administrador'},
                    {'id': 2, 'nombre': 'Cajero'}
                ]
            }
        }
    }
})
def get_Rol():
    roles = UsuarioService.get_roles()
    return jsonify([rol.as_dict() for rol in roles])


@usuario_blueprint.route('/nuevoRol', methods=['POST'])
@swag_from({
    'tags':['ROLES'],
    'summary':'Crear Roles',
    'description':'Crear Roles',
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
                'application/json': {'id': 1, 'nombre': 'Adminstrador'}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def add_rol():
    data = request.get_json()
    rol = UsuarioService.add_rol(data)
    return jsonify(rol.as_dict()), 201

@usuario_blueprint.route('/eliminarRol', methods=['POST'])
@swag_from({
    'tags':['ROLES'],
    'summary':'Eliminar Roles',
    'description':'Eliminar Roles',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Eliminación Exitosa',
            'examples': {
                'application/json': {'id': 1, 'nombre': 'Adminstrador'}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def delete_rol():
    data = request.get_json()
    rol = UsuarioService.delete_rol(data)
    return jsonify(rol.as_dict()), 201