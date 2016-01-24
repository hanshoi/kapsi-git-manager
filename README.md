# Kapsi Git Manager
Simple app for configuring and handling git repostitories in kapsi.fi. Applications handles user access and shows all repositories available in
git repository folder, and their ssh clone url. Also you can make new repositories there.

This is not meant to be general purpose or to work elsewhere, just to help those others who are using the same combination.

### Installing

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
  1. `cp kgm.conf ~/`
  2. `cp .htaccess ~/sites/USERNAME.kapsi.fi/secure-www/kgm`
  3. `cp .mysite.fcgi ~/sites/USERNAME.kapsi.fi/secure-www/kgm`
11. change the CAPITALIZED text in ~/kgm.conf
12. change the CAPITALIZED text in ~/sites/USERNAME.kapsi.fi/secure-www/kgm/mysite.fcgi

virtualenv install this package there with setyp.py install.
then make configurations from the example_confs into your public_html/mysite folder and there change all text written in CAPS of mysite.fcgi into something else.

### Using
When you have done the installation part you should now have web page accessible in "https://USERNAME.kapsi.fi/kgm/", if not, you did something wrong (or the application is faulty, which ofcourse just can't be..)

## TODO
* Adding support for HTTPS access for git repositories and clone urls for those
* Adding role based view support for this application
* Combining users from this account and HTTPS git access
* Make repo descriptions available
* Make a easier installation (with makefiles perhaps..)

## Contributing
Anyone who has the enthusiasm and skill is allowed to contribute. Just fork the repo and make a pull request to this one and I will add it.

### Development Environment
1. make a virtualenvironment and activate it
  1. install necessary requirements `sudo pip install virtualenv virtualenvwrapper`
  2. make virtualenv `mkvirtualenv myenv`
  3. start using it `workon myenv`
2. `pip install requirements.txt`
3. `python main.py`     (opens app in localhost:5000)

This is all, you are ready to roll.

Note: if you at any point want to stop using your virtualenv just run the command `deactivate`

#### Autoenv (optional)
Installing and using autoenv is optional completely, however a good tool in a lazy developers toolbox (and you know who you are..).

1. install autoenv in your system `sudo pip install autoenv`
2. run the following command in project root directory `echo "workon myenv" > .env`

Now you should be having a file called .env in your project root and command `workon myenv` within it. This will automatically enable myenv virtualenvironment
when you enter project directory tree (or any other command you deign to put there). It will not however `deactivate` it for you when you leave.

### Testing
1. run `pip install -e` in root directory
2. run `py.test` from root directory