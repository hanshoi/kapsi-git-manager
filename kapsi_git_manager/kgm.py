from flask import Flask, request, redirect, render_template, url_for, flash

from authentication import requires_auth

app = Flask(__name__)


# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
))
app.config.from_envvar('KGM_SETTINGS', silent=True)


@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/home')
@requires_auth
def home():
    flash("you are authed")
    return render_template('layout.html')


if __name__ == '__main__':
    app.run()
