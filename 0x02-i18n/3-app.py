#!/usr/bin/env python3
"""
flask module with i18n and l10n
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Flask babel configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """retrieve best lang match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """index page to say hello"""
    return render_template("3-index.html")


if __name__ == "__main__":
