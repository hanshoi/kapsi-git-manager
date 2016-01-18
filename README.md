# kapsi-git-manager
Simple app for configuring and handling git repostitories in kapsi.fi. Applications handles user access and shows all repositories available in
git repository folder, and their ssh clone url. Also you can make new repositories there.

This is not meant to be general purpose or to work elsewhere, just to help those others who are using the same combination.

## Installing
* make virtual environment for python 'virtualenv --python=/usr/bin/python2.7' ~/.env'
* activate it 'source ~/.env/bin/activate'
* load code as tar

virtualenv install this package there with setyp.py install.
then make configurations from the example_confs into your public_html/mysite folder and there change all text written in CAPS of mysite.fcgi into something else.

## Using


# TODO
* Adding support for HTTPS access for git repositories and clone urls for those
* Adding role based view support for this application
* Combining users from this account and HTTPS git access
* Make repo descriptions available

# Contributing
Anyone who has the enthusiasm and skill is allowed to contribute. Just fork the repo and make a pull request to this one and I will add it.

## Development Environment
* make a virtualenvironment and activate it
* pip install requirements.txt
* python main.py     (opens app in localhost:5000)

This is all, you are ready to roll.

## Testing
* pip install -r
* py.test  (executed from git root directory)