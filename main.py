#!/usr/bin/python

from flask import Flask, request, jsonify, Response, json
from Calcul import Calcul
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'


def getParameters(formDict):
    numbers = []
    keys = sorted(formDict)
    parametersDict = formDict

    for key in keys:
        numbers.append(parametersDict[key])
    return numbers

@app.route('/addition', methods=['POST'])
def addition():
    calc = Calcul()
    result = ""
    if request.method == "POST":
        calc.setNumbers(getParameters(request.form.to_dict()))
    calc.doOperation('+')
    result = calc.getResults()
    return result

@app.route('/soustraction', methods=['POST'])
def soustraction():
    calc = Calcul()
    result = ""
    if request.method == "POST":
        calc.setNumbers(getParameters(request.form.to_dict()))
    calc.doOperation('-')
    result = calc.getResults()
    return result

@app.route('/multiplication', methods=['POST'])
def multiplication():
    calc = Calcul()
    result = ""
    if request.method == "POST":
        calc.setNumbers(getParameters(request.form.to_dict()))
    calc.doOperation('*')
    result = calc.getResults()
    return result

@app.route('/division', methods=['POST'])
def division():
    calc = Calcul()
    result = ""
    if request.method == "POST":
        calc.setNumbers(getParameters(request.form.to_dict()))
    calc.doOperation('/')
    result = calc.getResults()
    return result

if __name__ == '__main__':
 app.run(host="0.0.0.0", port=8080)
