from __future__ import absolute_import
import os
import logging
from functools import wraps

from flask import Flask, request, redirect, render_template, url_for, flash

from .git_utils import get_repos, create_repo
from .authentication import auth

app = Flask(__name__)

# configuration
SECRET_KEY = 'development key'
GIT_FOLDER = os.path.dirname(os.path.dirname(__file__))
CREDENTIAL_FILE = os.path.join('tests', 'test.passwd')

app.config.from_object(__name__)
app.config.from_envvar('KGM_SETTINGS', silent=True)

logging.basicConfig(filename='kgm.log', level=logging.INFO)


def user_access_log(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        logging.info("%s accessed web page {}".format(f.__name__),
                     request.authorization.username)
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def index():
    logging.debug("accessed index page")
    return render_template('layout.html', authed=False)


@app.route('/home')
@auth.login_required
@user_access_log
def home():
    repo_folder = app.config["GIT_FOLDER"]
    repos = get_repos(repo_folder)
    return render_template('show_repos.html', authed=True, repos=repos)


@app.route('/add_repo', methods=["POST"])
@auth.login_required
@user_access_log
def add_repo():
    repo_name = request.form["name"]
    create_repo(os.path.join(app.config["GIT_FOLDER"], "{}.git".format(repo_name)))
    flash("New repo {} created!".format(repo_name))
    logging.info("New repo %s created!", repo_name)
    return redirect(url_for("home"))
