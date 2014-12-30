from app.models import db, security
from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from flask.ext.babel import format_datetime
import os


def create_app(name, settings=None):
    app = Flask(name)
    app.config.from_object('app.config')

    return app

