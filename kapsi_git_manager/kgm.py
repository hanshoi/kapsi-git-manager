from __future__ import absolute_import
import os

from flask import Flask, request, redirect, render_template, url_for, flash
from .authentication import auth
from .git_utils import get_repos, create_repo

app = Flask(__name__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# configuration
SECRET_KEY = 'development key'
GIT_FOLDER = PROJECT_ROOT

app.config.from_object(__name__)
app.config.from_envvar('KGM_SETTINGS', silent=True)


@app.route('/')
def index():
    return render_template('layout.html', authed=False)


@app.route('/home')
@auth.login_required
def home():
    repos = get_repos(app.config["GIT_FOLDER"])
    return render_template('show_repos.html', authed=True, repos=repos)


@app.route('/add_repo', methods=["POST"])
@auth.login_required
def add_repo():
    repo_name = request.form["name"]
    create_repo(os.path.join(app.config["GIT_FOLDER"], "{}.git".format(repo_name)))
    flash("New repo {} created!".format(repo_name))
    return redirect(url_for("home"))
