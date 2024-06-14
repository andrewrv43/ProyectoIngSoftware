from repositorio.usuarios_repos import UsuarioRepository
from modelos.tablas import usuarios,roles

class UsuarioService:

    @staticmethod
    def get_all_usuarios():
        return UsuarioRepository.get_all_usuarios()

    @staticmethod
    def get_usuario_by_id(usuario_id):
        return UsuarioRepository.get_usuario_by_id(usuario_id)

    @staticmethod
    def add_usuario(data):
        new_usuario = usuarios(nombre=data['nombre'], cedula=data['cedula'], id_rol=data['id_rol'])
        UsuarioRepository.add_usuario(new_usuario)
        return new_usuario

    @staticmethod
    def update_usuario(usuario_id, data):
        usuario = UsuarioRepository.get_usuario_by_id(usuario_id)
        if usuario:
            usuario.nombre = data['nombre']
            usuario.cedula = data.get('cedula')
            usuario.id_rol = data['id_rol']
            UsuarioRepository.update_usuario()
            return usuario
        return None

    @staticmethod
    def delete_usuario(usuario_id):
        usuario = UsuarioRepository.get_usuario_by_id(usuario_id['id'])
        if usuario:
            UsuarioRepository.delete_usuario(usuario)
            return usuario
        return None

    @staticmethod
    def get_roles():
        return UsuarioRepository.get_roles()