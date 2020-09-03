#!/usr/bin/python3
''' script that starts a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def all_states():
    ''' return all states '''
    states = storage.all(State).values()
    return (render_template('10-hbnb_filters.html', states=states))



@app.teardown_appcontext
def teardown_db(error):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

