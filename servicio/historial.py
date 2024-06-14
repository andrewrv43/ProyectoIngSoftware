from repositorio.historial_repos import HistorialRepository
from modelos.tablas import historial

class HistorialService:
    
    @staticmethod
    def get_all_historial():
        return HistorialRepository.get_all_historial()
    
    @staticmethod
    def get_historial_by_id(historial_id):
        return HistorialRepository.get_historial_by_id(historial_id)
    
    @staticmethod
    def add_historial(data):
        new_historial = historial(
            id_usuario=data['id_usuario'],
            productos=data['productos'],
            total=data['total']
        )
        HistorialRepository.add_usuario(new_historial)
        return new_historial
