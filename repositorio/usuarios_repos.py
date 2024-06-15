from modelos.tablas import usuarios, db,roles

class UsuarioRepository:

    @staticmethod
    def get_all_usuarios():
        return usuarios.query.all()

    @staticmethod
    def get_usuario_by_id(usuario_id):
        return usuarios.query.get(usuario_id)

    @staticmethod
    def add_usuario(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def update_usuario():
        db.session.commit()

    @staticmethod
    def delete_usuario(usuario):
        db.session.delete(usuario)
        db.session.commit()

    @staticmethod
    def get_roles():
        return roles.query.all()

    @staticmethod
    def add_rol(rol):
        db.session.add(rol)
        db.session.commit()