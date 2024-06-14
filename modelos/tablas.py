from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<Item {self.name}>'
    

class usuarios(db.Model):
    __tablename__ = 'tbl_usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    cedula = db.Column(db.String(10), nullable=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('tbl_rol.id'), nullable=False)

    def __repr__(self):
        return f'<usuarios {self.nombre}>'
    
    def as_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cedula': self.cedula,
            'id_rol': self.id_rol
        }
    
class roles(db.Model):
    __tablename__ = 'tbl_rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    
    def as_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
        }