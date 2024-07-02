#!/usr/bin/env python3
""" module flask """
from flask_babel import Babel
from flask import Flask, render_template, request


@babel.localeselector
def get_locale() -> str:
    """ get locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config:
    """ configuration file """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
