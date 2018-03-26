#!/bin/bash

# For System
sudo apt-get -y update
sudo apt-get -y upgrade

# For Python and pip
sudo apt-get install -y build-essential libssl-dev libffi-dev
sudo apt-get install -y python-dev python3-dev python python3
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade pip

# For Ganglia

## Ganglia Client 
sudo apt-get install -y ganglia-monitor

## Ganglia Master Node
## Install LAMP on your server
sudo apt-get install -y apache2 mariadb-server 
sudo apt-get install -y php7.0 libapache2-mod-php7.0 php7.0-mbstring php7.0-curl php7.0-zip php7.0-gd php7.0-mysql php7.0-curl php7.0-mcrypt

sudo systemctl start apache2 
sudo systemctl enable apache2

sudo apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend







