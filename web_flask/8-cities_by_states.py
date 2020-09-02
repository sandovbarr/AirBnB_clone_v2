#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' return all states '''
    cities_by_s = storage.all(State).values()
    return (render_template('8-cities_by_states.html', states=cities_by_s))


@app.teardown_appcontext
def teardown_db(error):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
