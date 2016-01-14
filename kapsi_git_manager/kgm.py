from __future__ import absolute_import

from flask import Flask, request, redirect, render_template, url_for, flash
from .authentication import auth

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('layout.html', authed=False)


@app.route('/home')
@auth.login_required
def home():
    return render_template('layout.html', authed=True)
