from flask import Flask, jsonify, request
from flask_cors import cross_origin
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/ingresar_sala": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/ingresar_sala', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def consul():
	return "hola"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
