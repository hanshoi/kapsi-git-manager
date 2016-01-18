import base64
import pytest
import shutil

from flask import Flask
from werkzeug.datastructures import Headers
from kapsi_git_manager import kgm


@pytest.fixture
def credentials(scope="module"):
    """
    Note that these credentials match those mentioned in test.htpasswd
    """
    h = Headers()
    h.add('Authorization',
          'Basic ' + base64.b64encode("username:password"))
    return h


def test_app_creation():
    assert isinstance(kgm.app, Flask) is True


def test_conf_params():
    """ test that all config params are present as required """
    conf = kgm.app.config
    assert conf["SECRET_KEY"] == "development key"
    assert conf["GIT_FOLDER"] is not None
    assert conf["CREDENTIAL_FILE"] is not None


def test_get_index():
    with kgm.app.test_client() as c:
        response = c.get("/")
        assert response.status_code == 200


def test_get_home_no_auth():
    with kgm.app.test_client() as c:
        response = c.get("/home")
        assert response.status_code == 401


def test_get_home_auth(credentials):
    with kgm.app.test_client() as c:
        response = c.get("/home", headers=credentials)
        assert response.status_code == 200


def test_add_repo(credentials):
    with kgm.app.test_client() as c:
        response = c.post("/add_repo", headers=credentials,
                          data={"name": "myrepo"})
        assert response.status_code == 302  # redirection url
    shutil.rmtree("myrepo.git")
