from repositorio.productos_repos import ProductoRepository
from modelos.tablas import productos, proveedores,roles

class ProductoService:

    @staticmethod
    def get_all_productos():
        return ProductoRepository.get_all_productos()

    @staticmethod
    def get_producto_by_id(producto_id):
        return ProductoRepository.get_producto_by_id(producto_id)

    @staticmethod
    def add_producto(data):
        new_producto = productos(nombre=data['nombre'], stock=data['stock'], precio=data['precio'], id_proveedor=data['id_proveedor'])
        ProductoRepository.add_producto(new_producto)
        return new_producto

    @staticmethod
    def update_producto(producto_id, data):
        producto = ProductoRepository.get_producto_by_id(producto_id)
        if producto:
            producto.nombre = data['nombre']
            producto.stock = data['stock']
            producto.precio = data['precio']
            producto.id_proveedor = data['id_proveedor']
            ProductoRepository.update_producto()
            return producto
        return None

    @staticmethod
    def delete_producto(producto_id):
        producto = ProductoRepository.get_producto_by_id(producto_id['id'])
        if producto:
            ProductoRepository.delete_producto(producto)
            return producto
        return None

    @staticmethod
    def get_Proveedores():
        return ProductoRepository.get_Proveedores()
    
    @staticmethod
    def add_Proveedor(data):
        new_proveedor = proveedores(nombre=data['nombre'])
        ProductoRepository.add_proveedor(new_proveedor)
        return new_proveedor
    
    @staticmethod
    def delete_proveedores(proveedor_id):
        proveedor = ProductoRepository.get_proveedor_by_id(proveedor_id['id'])
        if proveedor:
            ProductoRepository.delete_proveedor(proveedor)
            return proveedor
        return None