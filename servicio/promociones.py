from repositorio.promociones_repos import PromocionesRepository
from modelos.tablas import promociones,roles

class PromocionesService:

    @staticmethod
    def get_all_promociones():
        return PromocionesRepository.get_all_promociones()

    @staticmethod
    def get_promociones_by_id(promociones_id):
        return PromocionesRepository.get_promociones_by_id(promociones_id)

    @staticmethod
    def add_promociones(data):
        new_promociones = promociones(id_producto=data['id_producto'], porcentaje=data['porcentaje'])
        PromocionesRepository.add_promociones(new_promociones)
        return new_promociones

    @staticmethod
    def update_promociones(promociones_id, data):
        promociones = PromocionesRepository.get_promociones_by_id(promociones_id)
        if promociones:
            promociones.id_producto = data['id_producto']
            promociones.porcentaje = data.get('porcentaje')
            PromocionesRepository.update_promociones()
            return promociones
        return None

    @staticmethod
    def delete_promociones(promociones_id):
        promociones = PromocionesRepository.get_promociones_by_id(promociones_id['id'])
        if promociones:
            PromocionesRepository.delete_promociones(promociones)
            return promociones
        return None