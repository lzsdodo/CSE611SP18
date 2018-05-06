#!/bin/bash

# For Python and pip
sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get install -y python python-dev python3 python3-dev
sudo apt-get install -y python-setuptools 
sudo apt-get clean


# Install Python3.6
mkdir -p ~/opt && cd ~/opt
wget -c https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar -xvf Python-3.6.3.tgz
cd Python-3.6.3
sudo ./configure --enable-optimizations
sudo make
sudo make install
cd ~ && sudo rm -r ~/opt


# pip
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip
sudo pip install --upgrade pip


# venv
sudo apt-get install -y python-virtualenv
mkdir -p ~/venv/ && cd ~/venv
virtualenv --no-site-packages -p python3.6 py3

cd ~
source ~/venv/py3/bin/activate
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/script/pip_requirement.txt
pip install -r pip_requirement.txt
#pip freeze > pip_requirement.txt
#deactivate
rm pip_requirement.txt