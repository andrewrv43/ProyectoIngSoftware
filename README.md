
Para iniciar este proyecto se debe instalar los requerimientos usando: pip install -r requirements.txt .
Paso 2:
(Previamente se debe tener instalado python y haberlo agregado al PATH)
Iniciar la aplicación: python app.py

Ademas incluimos para este repositorio nuestra coleccion en postman la cual nos ayuda a probar nuestros endpoints de manera local.
Para poder hacer test de nuestra API usaremos el siguiente link:
https://accused-hedwig-sajaremastered-673fe6dd.koyeb.app/apidocs
Nos apoyamos en Koyeb para poder desplegar nuestra API.

Despues de instalar las librerias
pordemos ejecutar el siguiente comando:
pytest --cov=. --cov-report html:htmlcov . 
el cual nos generará los porcentajes de test de la api.
