from __future__ import absolute_import
import os
import logging

from flask import Flask, request, redirect, render_template, url_for, flash
from flask_httpauth import HTTPBasicAuth

from .git_utils import get_repos, create_repo

app = Flask(__name__)
auth = HTTPBasicAuth()

# configuration
SECRET_KEY = 'development key'
GIT_FOLDER = os.path.dirname(os.path.dirname(__file__))

app.config.from_object(__name__)
app.config.from_envvar('KGM_SETTINGS', silent=True)

logging.basicConfig(filename='kgm.log', level=logging.DEBUG)

users = {
    "admin": "secret",
}


@auth.get_password
def get_pw(username):
    """ return password or None if there isn't one"""
    if username in users:
        return users.get(username)
    logging.warning("%s tried to login with wrong password", username)
    return None


@app.route('/')
def index():
    logging.debug("accessed index page")
    return render_template('layout.html', authed=False)


@app.route('/home')
@auth.login_required
def home():
    logging.debug("accessed home page with all the fun repos!")
    repos = get_repos(app.config["GIT_FOLDER"])
    return render_template('show_repos.html', authed=True, repos=repos)


@app.route('/add_repo', methods=["POST"])
@auth.login_required
def add_repo():
    repo_name = request.form["name"]
    create_repo(os.path.join(app.config["GIT_FOLDER"], "{}.git".format(repo_name)))
    flash("New repo {} created!".format(repo_name))
    logging.info("New repo %s created!", repo_name)
    return redirect(url_for("home"))
