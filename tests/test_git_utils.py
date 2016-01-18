from kapsi_git_manager import git_utils


def test_make_repo_class():
    repo = git_utils.KgmRepo("tests", "reponame")
    assert repo.name == "reponame"
    assert repo._repo is None
    assert repo.git_dir == "tests"


def test_ssh_url():
    """
    Tests that conversion from HTTP pathing to SSH pathing works and produces
    a clonable url.
    """
    repo = git_utils.KgmRepo("/var/www/userhome/testuser/codedir/reponame.git", "reponame")
    assert repo.ssh_url == "testuser@lakka.kapsi.fi:/home/users/testuser/codedir/reponame.git"


def test_get_repos(tmpdir):
    """
    Get all folders in given path that aren't hidden as KgmRepo instances.
    """
    tmpdir.mkdir("myrepo")
    tmpdir.join("my.txt")
    tmpdir.mkdir(".hidden")
    repos = git_utils.get_repos(str(tmpdir.realpath()))
    assert len(repos) == 1
    assert isinstance(repos[0], git_utils.KgmRepo)
    assert "myrepo" in [a.name for a in repos]


def test_no_repos(tmpdir):
    repos = git_utils.get_repos(str(tmpdir.realpath()))
    assert len(repos) == 0
