#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def all_states():
    ''' return all states '''
    states = storage.all(State).values()
    return (render_template('9-states.html', states=states))


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    ''' return all states by it's id '''
    states_id = storage.all()
    for k, v in states_id.items():
        print ("{}, {}\n\n".format(k, v))


@app.teardown_appcontext
def teardown_db(error):
    ''' remove the current SQLAlchemy Session '''
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
