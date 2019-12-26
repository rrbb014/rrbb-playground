#!/bin/bash
PYVERSION=3.7.6


# install pyenv

#sudo apt update
#sudo apt dist-upgrade 

#sudo apt install git curl

cd $HOME

echo =========================
echo install required packages
echo =========================

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo export PATH="$HOME/.pyenv/bin:$PATH" >> $HOME/.zshrc
echo 'eval "$(pyenv init -)"' >> $HOME/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.zshrc

pyenv install $PYVERSION
pyenv virtualenv $PYVERSION torch

pyenv activate torch
pip3 install -r requirements.txt --user
