#!/usr/bin/python3
"""
Starts a simple web application listening on 0.0.0.0:5000
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_Hbnb():
    return 'Hello HBNB!'
