#!/usr/bin/python3
"""
Starts a web application using a variable and specifying a default
for path based the variage
"""

from flask import Flask
from markupsafe import escape
from flask import render_template
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_Hbnb():
    """ Displays Hello HBNB """

    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Displays HBN """

    return 'HBNB'


@app.route('/c/<text>')
def use_var(text):
    """ Displays C concatinated with <text> replacing '_' with ' ' """
    # text = text.replace("_", " ")
    return f'C {escape(text)}'


@app.route('/python/')
@app.route('/python/<text>')
def use_existing_var(text='is cool'):
    """ Specifies a default value for text if /python/ has no value
    and displays Python <text>
    """
    return f'Python {escape(text)}'


@app.route('/number/<int:n>')
def use_var_int(n):
    """ If n is an integer displays 'n' is a number """

    if type(n) == int:
        return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>')
def display_page(n):
    if type(n) == int:
        """ Renders the 5-number.html page if n is an int """
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
