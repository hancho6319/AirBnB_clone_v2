#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)
