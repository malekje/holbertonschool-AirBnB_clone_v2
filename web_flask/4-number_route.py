#!/usr/bin/python3
"""
a script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text="is_cool"):
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def python_number(n):
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
