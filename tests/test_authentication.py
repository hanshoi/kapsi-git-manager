import pytest

from flask_httpauth import HTTPBasicAuth

from kapsi_git_manager.kgm import app
from kapsi_git_manager import authentication as auth


password = "password"
username = "username"


def test_auth_simple():
    """ this is the idiot test to check whether anything in you auth system works. """
    assert isinstance(auth.auth, HTTPBasicAuth)


def test_verify_correct_password():
    """ with the credentials file try to verify correct password combination """
    with app.app_context():
        assert auth.verify_pw(username, password) == True


def test_verify_wrong_password():
    """ with the credentials file try to verify wrong password combination. """
    with app.app_context():
        assert auth.verify_pw("winnie", "pooh") == False
