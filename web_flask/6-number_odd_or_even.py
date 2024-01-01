#!/usr/bin/python3
""" web application to /: display “Hello HBNB!”,
    /hbnb: display “HBNB”, and /c/<text>: display “C ”
"""


from flask import Flask, render_template
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


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Return reformatted with the replaced
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_it_a_number(n=None):
    """Return string when route queried
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Return an HTML page
    """
    return render_template('5-number.html', value=n)

@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Return an HTML page with is wether
       the n value odd or even
    """
    msg = "even" if n%2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', value=n, string=msg)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
