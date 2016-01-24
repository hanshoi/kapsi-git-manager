# kapsi-git-manager
Simple app for configuring and handling git repostitories in kapsi.fi. Applications handles user access and shows all repositories available in
git repository folder, and their ssh clone url. Also you can make new repositories there.

This is not meant to be general purpose or to work elsewhere, just to help those others who are using the same combination.

## Installing

1. make virtual environment for python `virtualenv --python=/usr/bin/python2.7' ~/.env`
2. activate it `source ~/.env/bin/activate`
3. load code as zip to server `wget https://github.com/hanshoi/kapsi-git-manager/archive/master.zip`
4. extract it `unzip master.zip`
5. go to the newly extracted folder `cd kapsi-git-manager-master`
6. install kapsi-git-manager by running `python setup.py install`
7. make dir for https access `mkdir ~/sites/USERNAME.kapsi.fi/secure-www/kgm`
8. make a git folder `mkdir ~/code` (any other folder goes as well)
9. make password file `htpasswd -c ~/.kgm.htpasswd USERNAME`
10. copy following files from example_confs
  10.1. `cp kgm.conf ~/`
  10.2. `cp .htaccess ~/sites/USERNAME.kapsi.fi/secure-www/kgm`
  10.3. `cp .mysite.fcgi ~/sites/USERNAME.kapsi.fi/secure-www/kgm`
11. change the CAPITALIZED text in ~/kgm.conf
12. change the CAPITALIZED text in ~/sites/USERNAME.kapsi.fi/secure-www/kgm/mysite.fcgi

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
1. make a virtualenvironment and activate it
2. pip install requirements.txt
3. python main.py     (opens app in localhost:5000)

This is all, you are ready to roll.

## Testing
1. pip install -r
2. py.test  (executed from git root directory)