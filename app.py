from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    A simple hello world endpoint
    ---
    responses:
      200:
        description: A successful response
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify(message="Hello, World!")

@app.route('/echo', methods=['POST'])
def echo():
    """
    Echo back the received JSON
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello, Echo!"
    responses:
      200:
        description: A successful response
        examples:
          application/json: {"message": "Hello, Echo!"}
    """
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
