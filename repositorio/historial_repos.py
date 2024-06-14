from modelos.tablas import historial,db

class HistorialRepository:

    @staticmethod
    def get_all_historial():
        return historial.query.all()
    
    @staticmethod
    def get_historial_by_id(historial_id):
        return historial.query.get(historial_id)
    
    @staticmethod
    def add_usuario(historial):
        db.session.add(historial)
        db.session.commit()

    @staticmethod
    def delete_historial(historial_id):
        historial_a_eliminar = historial.query.get(historial_id)
        if historial_a_eliminar:
            db.session.delete(historial_a_eliminar)
            db.session.commit()
            return True
        return False