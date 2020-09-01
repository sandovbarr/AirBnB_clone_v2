#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    ''' return for index location '''
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbtn():
    ''' return for hbth location '''
    return ("HBNB")


if __name__ == '__main__':
    app.run()
