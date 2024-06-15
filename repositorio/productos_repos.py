from modelos.tablas import productos, db, proveedores

class ProductoRepository:

    @staticmethod
    def get_all_productos():
        return productos.query.all()

    @staticmethod
    def get_producto_by_id(producto_id):
        return productos.query.get(producto_id)

    @staticmethod
    def add_producto(producto):
        db.session.add(producto)
        db.session.commit()

    @staticmethod
    def update_producto():
        db.session.commit()

    @staticmethod
    def delete_producto(producto):
        db.session.delete(producto)
        db.session.commit()

    @staticmethod
    def get_Proveedores():
        return proveedores.query.all()
    
    @staticmethod
    def add_proveedor(proveedor):
        db.session.add(proveedor)
        db.session.commit()

    @staticmethod
    def get_proveedor_by_id(proveedor_id):
        return proveedores.query.get(proveedor_id)

    @staticmethod
    def delete_proveedor(proveedor):
        db.session.delete(proveedor)
        db.session.commit()