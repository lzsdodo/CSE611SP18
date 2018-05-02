#!/bin/bash

sudo apt-get update
sudo apt-get install -y build-essential libpq-dev libssl-dev openssl libffi-dev zlib1g-dev
sudo apt-get install -y python3-pip python3-dev

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

