#!/usr/bin/env python3
""" module flask """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """ return a html page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
