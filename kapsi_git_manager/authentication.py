import logging
from passlib.apache import HtpasswdFile

from flask_httpauth import HTTPBasicAuth
from flask import current_app as app

auth = HTTPBasicAuth()


@auth.verify_password
def verify_pw(username, password):
    """ return password or None if there isn't one"""
    credentials = HtpasswdFile(app.config["CREDENTIAL_FILE"])
    if not credentials.check_password(username, password):
        logging.warning("%s tried to login with wrong password", username)
        return False
    return True
