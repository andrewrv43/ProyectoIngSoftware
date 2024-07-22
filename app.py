from flask import Flask
from flasgger import Swagger
from modelos.tablas import db
from config import Config
from controlador.usuarios_control import usuario_blueprint
from controlador.productos_control import producto_blueprint
from controlador.historial_control import historial_blueprint
from controlador.promociones_control import promociones_blueprint
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    swagger = Swagger(app)
    CORS(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(producto_blueprint)
    app.register_blueprint(historial_blueprint)
    app.register_blueprint(promociones_blueprint)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000,debug=True)
