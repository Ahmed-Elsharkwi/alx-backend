#!/usr/bin/env python3
""" module flask """
from typing import Dict, Union
from flask_babel import Babel
from flask import Flask, render_template, request, g
import pytz

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ configuration file """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ get locale """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = get_user()

    if user is not None and user["locale"] in app.config['LANGUAGES']:
        return user["locale"]

    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ get the time """
    try:
        one = request.args.get('timezone')
        if one is not None:
            return pytz.timezone(one).zone

        user = get_user()
        if user is not None:
            return pytz.timezone(user["timezone"]).zone

    except pytz.exceptions.UnknownTimeZoneError:
        return request.accept_languages.best_match(app.config[
            'BABEL_DEFAULT_TIMEZONE'])


def get_user() -> Union[Dict, None]:
    """ get the user info """
    user_id = request.args.get('login_as')
    if user_id is not None:
        for id_1 in users:
            if int(user_id) == id_1:
                return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """ function which will be executed before all functions
    """
    res = get_user()
    g.user = res["name"]


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
