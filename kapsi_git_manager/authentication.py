import logging

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "admin": "secret",
}


@auth.get_password
def get_pw(username):
    """ return password or None if there isn't one"""
    if username in users:
        return users.get(username)
    logging.warning("%s tried to login with wrong passwod", username)
    return None
