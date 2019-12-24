#!/bin/bash
PYVERSION=3.7.6

# install pyenv

sudo apt update
sudo apt dist-upgrade 

sudo apt install git curl

cd $HOME

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

exec $SHELL

pyenv install $PYVERSION
pyenv virtualenv $PYVERSION torch

echo "Check pyenv versions"
