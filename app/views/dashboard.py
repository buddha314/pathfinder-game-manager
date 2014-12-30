from . import bp
from flask import render_template, redirect, url_for

@bp.route('/')
def dashboard():
    return render_template("dashboard.html")