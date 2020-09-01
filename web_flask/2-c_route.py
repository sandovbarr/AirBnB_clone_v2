#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' return for index location '''
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbtn():
    ''' return for hbth location '''
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def r_text(text):
    ''' show text variable'''
    text = text.replace("_", " ")
    return ('C %s' % escape(text))


if __name__ == '__main__':
    app.run()
