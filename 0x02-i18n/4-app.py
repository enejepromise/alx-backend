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
