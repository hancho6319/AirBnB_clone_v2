#!/usr/bin/python3
""" web application to /: display “Hello HBNB!”,
    /hbnb: display “HBNB”, and /c/<text>: display “C ”
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted with the replace
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text=“is cool”):
    """Return reformatted with the replaced
    """
    return “Python ” + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
