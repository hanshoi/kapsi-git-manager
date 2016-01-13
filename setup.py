import os
from setuptools import setup


def read(fname):
    """
    Read README.md as long description if found.
    Otherwise just return short description.
    """
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return "Simple git management application to be used in Kapsi hosting."

setup(
    name="kapsi_git_manager",
    version="0.0.1",
    author="Antti Ruotsalainen",
    author_email="antti.ruotsalainen@hanshoi.net",
    description=("Simple git management application to be used in Kapsi hosting."),
    license="MIT",
    keywords="git management kapsi",
    url="http://packages.python.org/kapsi_git_manager",
    packages=['kapsi_git_manager'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
