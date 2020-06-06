from flask import Flask, jsonify, request
from flask_cors import cross_origin
from flask_cors import CORS
app = Flask(__name__)

cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def consul():
	return "{'1': {'semestre': 15, 'correo': 'royer123@gmail.com', 'celular': 123, 'nombre': 'Royer', 'password': 'hola', 'id': 1234}, '0': {'semestre': 8, 'correo': 'luchocorrealviveros@gmail.com', 'celular': 3148527176, 'nombre': 'Luis', 'password': 'hola', 'id': 1116282977}, '2': {'semestre': 8, 'correo': 'gian123@gmail.com', 'celular': 123, 'nombre': 'gian', 'password': 'hola', 'id': 123}}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
