from flask import Flask
from flasgger import Swagger
from modelos.tablas import db
from config import Config
from controlador.usuarios_control import usuario_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
swagger = Swagger(app)

app.register_blueprint(usuario_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
