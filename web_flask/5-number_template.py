#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, escape, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_text(text='is cool'):
    '''
        display “Python ”,
        followed by the value of
        the text variable
    '''
    text = text.replace("_", " ")
    return ('Python %s' % escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Return n if it's number '''
    return ('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' Return n if it's number '''
    return (render_template('5-number.html', num=n))


if __name__ == '__main__':
    app.run()
