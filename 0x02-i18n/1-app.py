#!/usr/bin/env python3
""" module flask """
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """ configuration file """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)