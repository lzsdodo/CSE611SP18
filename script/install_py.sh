#!/bin/bash

# For Python and pip
sudo apt-get update
sudo apt-get -y install build-essential libpq-dev libssl-dev libffi-dev openssl zlib1g-dev bazel
sudo apt-get -y install python python-dev python3 python3-dev 
sudo apt-get -y install python3-pip python-virtualenv
sudo apt-get -y install pkg-config zip g++ unzip
sudo pip3 -y install --upgrade pip

# Install Python3.6
# Method 1: Using PPA
#sudo add-apt-repository ppa:jonathonf/python-3.6
#sudo apt-get update
#sudo apt-get install -y python3.6

# Method 2: Download and configure
mkdir -p ~/opt && cd ~/opt
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar -xvf Python-3.6.3.tgz
cd Python-3.6.3
sudo ./configure --enable-optimizations
sudo make && make install
cd ~ && rm -r ~/opt


# venv