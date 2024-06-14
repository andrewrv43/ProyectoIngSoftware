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

class proveedores(db.Model):
    __tablename__ = 'tbl_proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    
    def as_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
        }
class productos(db.Model):
    __tablename__ = 'tbl_producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=True)
    precio = db.Column(db.Float, nullable=True)
    id_proveedor = db.Column(db.Integer, db.ForeignKey('tbl_proveedor.id'), nullable=False)

    def __repr__(self):
        return f'<productos {self.nombre}>'
    
    def as_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'stock': self.stock,
            'precio': self.precio,
            'id_proveedor': self.id_proveedor
        }

class historial(db.Model):
    __tablename__ = 'tbl_historial'
    id=db.Column(db.Integer, primary_key=True)
    id_usuario=db.Column(db.Integer, nullable=True)
    productos=db.Column(db.String(1000), nullable=True)
    total=db.Column(db.Double, nullable=True)

    def __repr__(self):
        return f'<historial {self.id_usuario}>'
    
    def as_dict(self):
        return {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'productos': self.productos,
            'total': self.total
        }
