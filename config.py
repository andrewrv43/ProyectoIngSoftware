import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title': 'API PARA LA GESTION DE MICROMERCADO',
        'description': 'Aqui definimos la gestion de usuarios roles, creacion de productos informacion de proveedores y más.'
    }