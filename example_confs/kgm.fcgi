#!/home/users/MYUSERNAME/MYVIRTUALENV/bin/python

# vars
USERNAME="MYUSERNAME"
VIRTUAL_ENV_BIN = "/home/users/{}/MYVIRTUALENV/bin".format(USERNAME)
SITE_PATH = "/home/users/{0}/sites/{0}.kapsi.fi/secure-www/MYSITE".format(USERNAME)

# Set up the virtual environment:
import os, sys
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = VIRTUAL_ENV_BIN+':' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = VIRTUAL_ENV_BIN
os.environ['PYTHON_EGG_CACHE'] = VIRTUAL_ENV_BIN
os.chdir(SITE_PATH)

# Add a custom Python path.
sys.path.insert(0, SITE_PATH)

# FCGI part
from flup.server.fcgi import WSGIServer
from kapsi_git_manager import app

if __name__ == '__main__':
    WSGIServer(app).run()
