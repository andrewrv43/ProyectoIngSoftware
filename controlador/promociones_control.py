from flask import Blueprint, jsonify, request
from servicio.promociones import *
from flasgger import swag_from

promociones_blueprint = Blueprint('promociones', __name__)

################################################################################
#                           PROMOCIONES                                        #
################################################################################

@promociones_blueprint.route('/promociones', methods=['GET'])
@swag_from({
    'tags':['PROMOCIONES'],
    'summary':'Obtener una lista de promociones',
    'description':'Obtener una lista de promociones',
    'responses': {
        200: {
            'description': 'Una lista de promociones',
            'examples': {
                'application/json': [
                    {'id': 1, 'id_producto': 1, 'porcentaje': 50},
                    {'id': 2, 'id_producto': 2, 'porcentaje': 12}
                ]
            }
        }
    }
})
def get_promociones():
    promociones = PromocionesService.get_all_promociones()
    return jsonify([promociones.as_dict() for promociones in promociones])



@promociones_blueprint.route('/nuevaPromocion', methods=['POST'])
@swag_from({
    'tags':['PROMOCIONES'],
    'summary':'Crear una nueva promoción',
    'description':'Crear una nueva promoción',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id_producto': {'type': 'integer'},
                    'procentaje': {'type': 'integer'},
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Creación Exitosa',
            'examples': {
                'application/json': {'id': 1, 'id_producto': 1, 'porcentaje': 12}
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def add_promociones():
    data = request.get_json()
    promociones = PromocionesService.add_promociones(data)
    return jsonify(promociones.as_dict()), 201

@promociones_blueprint.route('/eliminarPromocion', methods=['POST'])
@swag_from({
    'tags':['PROMOCIONES'],
    'summary':'Eliminar una promoción',
    'description':'Eliminar una promoción',
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
def delete_promociones():
    data = request.get_json()
    promociones = PromocionesService.delete_promociones(data)
    return jsonify(promociones.as_dict()), 200

@promociones_blueprint.route('/obtPromocion', methods=['POST'])
@swag_from({
    'tags':['PROMOCIONES'],
    'summary':'Obtener una Promoción especifica Por ID',
    'description':'Obtener una Promoción especifica Por ID',
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
                  'application/json':  {'id': 1, 'id_producto': 1, 'porcentaje': 50},
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def obtener_promociones():
    data = request.get_json()
    promociones = PromocionesService.get_promociones_by_id(data)
    return jsonify(promociones.as_dict()), 200
