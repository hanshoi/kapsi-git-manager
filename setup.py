import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="kapsi_git_manager",
    version="0.0.1",
    author="Antti Ruotsalainen",
    author_email="antti.ruotsalainen@hanshoi.net",
    description=("Simple git management application to be used in Kapsi hosting."),
    license="MIT",
    keywords="git management kapsi",
    url="http://packages.python.org/kapsi_git_manager",
    packages=['kapsi_git_manager', 'tests'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
