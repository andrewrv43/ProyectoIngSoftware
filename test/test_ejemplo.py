import json

#TEST ENDPOINTS USUARIOS

def test_get_usuarios(client):
    response = client.get('/usuarios')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_add_usuario(client):
    new_user = {
        'nombre': 'Andrew Rueda 2',
        'cedula': '1722225461',
        'id_rol': 2,
        'password': '12345'
    }
    response = client.post('/nuevoUsuario', json=new_user)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['nombre'] == 'Andrew Rueda 2'
    assert data['cedula'] == '1722225461'
    assert data['id_rol'] == 2
    assert data['password'] == '12345'

def test_delete_usuario(client):
    delete_id = {'id': 2}
    response = client.post('/eliminarUsuario', json=delete_id)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 2

def test_get_obtUsuario(client):
    get_id = {'id': 3}
    response = client.post('/obtUsuario', json=get_id)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == 3

#TEST ENDPOINTS ROLES

def test_get_obtRoles(client):
    response = client.get('/obtRoles')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_add_Rol(client):
    new_rol = {
        "nombre": "Rol Test"
    }
    response = client.post('/nuevoRol', json=new_rol)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['nombre'] == 'Rol Test'

def test_delete_rol(client):
    delete_id = {'id': 2}
    response = client.post('/eliminarRol', json=delete_id)
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['id'] == 2 
#TEST ENDPOINTS HITORIAL

def test_get_historial(client):
    response = client.get('/historial')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_historial(client):
    data = {
        'id_usuario': 1,
        'productos': 'Producto A, Producto B,pRODUCTOC',
        'total': 150.75
    }
    response = client.post('/nuevoHistorial',json=data)
    assert response.status_code == 201
    assert response.json['id_usuario'] == data['id_usuario']
    assert response.json['productos'] == data['productos']
    assert response.json['total'] == data['total']

def test_obtener_historial_id(client):
    data = {'id': 1}
    response = client.post('/obtHistorial', json=data)
    assert response.status_code == 200
    assert response.json['id'] == data['id']

#TEST ENDPOINTS PRODUCTOS

def test_get_productos(client):
    response = client.get('/productos')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_producto(client):
    data = {
        'nombre': 'Producto 2',
        'stock': 15,
        'precio': 5.75,
        'id_proveedor': 2
    }
    response = client.post('/nuevoProducto', json=data)
    assert response.status_code == 201
    assert response.json['nombre'] == data['nombre']
    assert response.json['stock'] == data['stock']
    assert response.json['precio'] == data['precio']
    assert response.json['id_proveedor'] == data['id_proveedor']

def test_delete_producto(client):
    data = {'id': 2}
    response = client.post('/eliminarProducto', json=data)
    assert response.status_code == 200
    assert response.json['id'] == data['id']

def test_obtener_producto_id(client):
    data = {'id': 3}
    response = client.post('/obtProducto', json=data)
    assert response.status_code == 200
    assert response.json['id'] == data['id']

#TEST ENDPOINTS PROVEEDORES

def test_get_Proveedor(client):
    response = client.get('/obtProveedores')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_proveedor(client):
    data = {'nombre':'Proveedor 2'}
    response = client.post('/nuevoProveedor', json=data)
    assert response.status_code == 201
    assert response.json['nombre'] == data['nombre']

def test_delete_proveedores(client):
    data = {'id': 2}
    response = client.post('/eliminarProveedor', json=data)
    assert response.status_code == 200
    assert response.json['id'] == data['id']

#TEST ENDPOINTS PROMOCIONES
def test_get_Promociones(client):
    response = client.get('/promociones')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_nueva_Promocion(client):
    data = {'id_producto':2,'porcentaje':20}
    response = client.post('/nuevaPromocion', json=data)
    assert response.status_code == 201
    assert response.json['porcentaje'] == data['porcentaje']

def test_delete_Promocion(client):
    data = {'id': 2}
    response = client.post('/eliminarPromocion', json=data)
    assert response.status_code == 200
    assert response.json['id'] == data['id']

def test_obtener_Promocion_id(client):
    data = {'id': 3}
    response = client.post('/obtPromocion', json=data)
    assert response.status_code == 200
    assert response.json['id'] == data['id']

