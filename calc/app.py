# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Home Page"

@app.route('/add')
def add_calc():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def sub_calc():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def mult_calc():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def div_calc():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))

MATH = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def math_calc(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(MATH[operation](a,b))
