from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "admin": "secret",
}


@auth.get_password
def get_pw(username):
    """ return password or None if there isn't one"""
    return users.get(username)
