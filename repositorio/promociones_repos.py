from modelos.tablas import promociones, db,roles

class PromocionesRepository:

    @staticmethod
    def get_all_promociones():
        return promociones.query.all()

    @staticmethod
    def get_promociones_by_id(promociones_id):
        return promociones.query.get(promociones_id)

    @staticmethod
    def add_promociones(promociones):
        db.session.add(promociones)
        db.session.commit()

    @staticmethod
    def update_promociones():
        db.session.commit()

    @staticmethod
    def delete_promociones(promociones):
        db.session.delete(promociones)
        db.session.commit()
