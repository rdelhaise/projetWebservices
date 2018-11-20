from flask import Flask, request, jsonify, Response, json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def operator(a, b, ope):
    result = None
    
    try:
        a = a.replace(",", ".")
        b = b.replace(",", ".")
        a = float(a)
        b = float(b)
        if ope == '+' :
            result = a + b
        elif ope == '-':
            result = a - b
        elif ope == '*' :
            result = a * b
        elif ope == '/':
            if b != 0.0 and a != 0.0:
                result = a / b
            else:
                result = "Il n'est pas possible de diviser par 0"
    except:
        result = "Veuillez revoir ce que vous envoyez, les variables sont a et b et ce doit etre des chiffres"
        
    
    
    return str(result)


@app.route('/addition', methods=['POST'])
def addition():
    result = ""
    a = 0
    b = 0
    if request.method == "POST":
            a = request.form['a']
            b = request.form['b']
    return operator(a, b, '+')

@app.route('/soustraction', methods=['POST'])
def soustraction():
    result = ""
    a = 0
    b = 0
    if request.method == "POST":
            a = request.form['a']
            b = request.form['b']
    return operator(a, b, '-')

@app.route('/multiplication', methods=['POST'])
def multiplication():
    result = ""
    a = 0
    b = 0
    if request.method == "POST":
            a = request.form['a']
            b = request.form['b']
    return operator(a, b, '*')

@app.route('/division', methods=['POST'])
def division():
    result = ""
    a = 0
    b = 0
    if request.method == "POST":
            a = request.form['a']
            b = request.form['b']
    return operator(a, b, '/')
