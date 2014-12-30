from .. import factory

from flask import Blueprint, render_template

bp = Blueprint('bp', __name__)

from .extensions import assets, babel
from . import dashboard

def create_app(name=None, settings=None):
    app = factory.create_app(name or __name__, settings=settings) 
    babel.init_app(app) 
    app.register_blueprint(bp)

    return app

