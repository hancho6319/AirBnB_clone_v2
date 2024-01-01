#!/usr/bin/python3

from web_flask import app

# Define a route for the root URL ('/')
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

