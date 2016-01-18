# kapsi-git-manager
Simple app for configuring and handling git repostitories in kapsi.fi. Applications handles user access and shows all repositories available in
git repository folder, and their ssh clone url. Also you can make new repositories there.

This is not meant to be general purpose or to work elsewhere, just to help those others who are using the same combination.

## Installing

* make virtual environment for python 'virtualenv --python=/usr/bin/python2.7' ~/.env'
* activate it 'source ~/.env/bin/activate'
* load code as zip to server 'wget https://github.com/hanshoi/kapsi-git-manager/archive/master.zip'
* extract it 'unzip master.zip'
* go to the newly extracted folder 'cd kapsi-git-manager-master'
* install kapsi-git-manager by running 'python setup.py install'
* make dir for https access 'mkdir ~/sites/USERNAME.kapsi.fi/secure-www/kgm'
* make a git folder 'mkdir ~/code' (any other folder goes as well)
* make password file 'htpasswd -c ~/.kgm.htpasswd USERNAME'
* copy following files from example_confs
** 'cp kgm.conf ~/'
** 'cp .htaccess ~/sites/USERNAME.kapsi.fi/secure-www/kgm'
** 'cp .mysite.fcgi ~/sites/USERNAME.kapsi.fi/secure-www/kgm'
* change the CAPITALIZED text in ~/kgm.conf
* change the CAPITALIZED text in ~/sites/USERNAME.kapsi.fi/secure-www/kgm/mysite.fcgi

virtualenv install this package there with setyp.py install.
then make configurations from the example_confs into your public_html/mysite folder and there change all text written in CAPS of mysite.fcgi into something else.

## Using
When you have done the installation part you should now have web page accessible in "https://USERNAME.kapsi.fi/kgm/", if not, you did something wrong (or the application is faulty, which ofcourse just can't be..)

# TODO
* Adding support for HTTPS access for git repositories and clone urls for those
* Adding role based view support for this application
* Combining users from this account and HTTPS git access
* Make repo descriptions available
* make a easier installation (with makefiles perhaps..)

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