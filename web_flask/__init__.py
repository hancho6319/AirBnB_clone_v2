#!/usr/bin/python3

from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Import the routes defined in hello.py
from app import 0-hello_route

if __name__ == "__main__":
    # Run the app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)

