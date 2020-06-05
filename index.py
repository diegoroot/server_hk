from flask import Flask, jsonify, request
from flask_cors import cross_origin
from flask_cors import CORS
app = Flask(__name__)

@app.route('/ingresar_sala', methods=['GET','POST'])
def consul():
	return "hola"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
