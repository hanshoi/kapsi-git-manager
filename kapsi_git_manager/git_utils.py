import os
from git import Repo
from os.path import isdir


class KgmRepo(object):
    def __init__(self, folder_path, name):
        self.name = name
        self.git_dir = folder_path
        self._repo = None

    @property
    def repo(self):
        if not self._repo:
            self._repo = Repo(os.path.join(self.git_dir, self.name))
        return self._repo

    @property
    def ssh_url(self):
        username = self.git_dir.replace('/home/users/', '').replace('/{}.git'.format(self.name), '')
        return "{0}@lakka.kapsi.fi:{1.git_dir}/{1.name}".format(username, self)


def get_repos(path):
    """
    Returns all folders in repository folder that are visible as KgmRepo objects.
    """
    repos = []
    for name in os.listdir(path):
        if isdir(name) and name[0] != '.':
            repos.append(KgmRepo(path, name))
    return repos


def create_repo(path):
    """
    Give the full path to then new repo with .git ending included.
    """
    repo = Repo.init(path, bare=True)
    return repo
