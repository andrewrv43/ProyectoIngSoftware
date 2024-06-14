from flask import Blueprint, jsonify, request
from servicio.historial import HistorialService
from flasgger import swag_from

historial_blueprint = Blueprint('historial', __name__)

################################################################################
#                           HISTORIAL                                           #
################################################################################

@historial_blueprint.route('/historial', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Una lista de historial',
            'examples': {
                'application/json': [
                    {'id': 1, 'id_usuario': 1, 'productos': 'Producto A, Producto B', 'total': 150.75},
                    {'id': 2, 'id_usuario': 2, 'productos': 'Producto C', 'total': 75.50},
                ]
            }
        }
    }
})

def get_historial():
    historial = HistorialService.get_all_historial()
    return jsonify([historial.as_dict() for historial in historial])


@historial_blueprint.route('/nuevoHistorial', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'id_usuario': {'type': 'integer'},
                    'productos': {'type': 'string'},
                    'total': {'type': 'number', 'format': 'double'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Creación Exitosa',
            'examples': {
                'application/json': {
                    'id': 1, 'id_usuario': 1, 'productos': 'Producto A, Producto B', 'total': 150.75
                }
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})

def add_historial():
    data = request.get_json()
    historial = HistorialService.add_historial(data)
    return jsonify(historial.as_dict()), 201

@historial_blueprint.route('/obtHistorial', methods=['POST'])
@swag_from({
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
            'description': 'Busqueda exitosa',
            'examples': {
                   'application/json': 
                   {'id': 1, 'id_usuario': 1, 'prodcutos':'Producto A, Prodcuto B', 'total':  150.75},
            }
        },
        400: {
            'description': 'Request Invalido'
        }
    }
})
def obtener_historial():
    data = request.get_json()
    historial = HistorialService.get_historial_by_id(data)
    return jsonify(historial.as_dict()),200