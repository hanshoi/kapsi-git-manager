from __future__ import absolute_import
import os

from flask import Flask, request, redirect, render_template, url_for, flash
from .authentication import auth

app = Flask(__name__)

# configuration
SECRET_KEY = 'development key'
GIT_FOLDER = os.path.join(os.path.abspath(__file__), 'git')

app.config.from_object(__name__)
app.config.from_envvar('KGM_SETTINGS', silent=True)


@app.route('/')
def index():
    return render_template('layout.html', authed=False)


@app.route('/home')
@auth.login_required
def home():
    return render_template('layout.html', authed=True)
