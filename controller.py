from flask import Flask, request, jsonify
from calculator import Calculator

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum():
    a =  request.args.get('a', default = 0.0, type = float)
    
    b =  request.args.get('b', default = 0.0, type = float)

    calc = Calculator()

    return jsonify(result=calc.sum(a, b))

@app.route('/subtract', methods=['GET'])
def subtract():
    a =  request.args.get('a', default = 0.0, type = float)
    
    b =  request.args.get('b', default = 0.0, type = float)

    calc = Calculator()

    return jsonify(result=calc.subtract(a, b))

@app.route('/multiply', methods=['GET'])
def multiply():
    a =  request.args.get('a', default = 0.0, type = float)
    
    b =  request.args.get('b', default = 0.0, type = float)

    calc = Calculator()

    return jsonify(result=calc.multiply(a, b))

@app.route('/divide', methods=['GET'])
def divide():
    a =  request.args.get('a', default = 0.0, type = float)
    
    b =  request.args.get('b', default = 0.0, type = float)

    calc = Calculator()

    return jsonify(result=calc.divide(a, b))