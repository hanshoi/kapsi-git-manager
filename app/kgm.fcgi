#!/home/users/hanshoi/envs/kgm/bin/python

# vars
VIRTUAL_ENV_BIN = "/home/users/hanshoi/envs/kgm/bin"
SITE_PATH = "/home/users/hanshoi/sites/hanshoi.kapsi.fi/secure-www/kgm"

# Set up the virtual environment:
import os, sys
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = VIRTUAL_ENV_BIN+':' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = VIRTUAL_ENV_BIN
os.environ['PYTHON_EGG_CACHE'] = VIRTUAL_ENV_BIN
os.chdir(SITE_PATH)

# Add a custom Python path.
sys.path.insert(0, SITE_PATH)


#!/usr/bin/python

from flup.server.fcgi import WSGIServer
from main import app

if __name__ == '__main__':
    WSGIServer(app).run()
