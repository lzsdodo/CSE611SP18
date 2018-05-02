#!/bin/bash

cd ~
mkdir script
mkdir code
mkdir data

# For System
sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get -y install software-properties-common

# For java
sudo apt-get -y install default-jre default-jdk
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get -y update
sudo apt-get -y install oracle-java8-installer
sudo update-alternatives --config java
#0
sudo vi /etc/environment
#JAVA_HOME="/usr/lib/jvm/java-8-oracle"
source /etc/environment
echo $JAVA_HOME


# For Python and pip
sudo apt-get -y install build-essential libssl-dev libffi-dev zlib1g-dev
sudo apt-get -y install python python-dev python3 python3-dev 
sudo apt-get -y install python3-pip python-virtualenv
sudo apt-get -y install pkg-config zip g++ unzip
sudo pip3 -y install --upgrade pip



# For Ganglia
## Ganglia Client 
sudo apt-get -y install ganglia-monitor

## Ganglia Master Node
## Install LAMP on your server
sudo apt-get -y install apache2 mariadb-server 
sudo apt-get -y install php7.0 libapache2-mod-php7.0 php7.0-mbstring php7.0-curl php7.0-zip php7.0-gd php7.0-mysql php7.0-mcrypt

sudo systemctl start apache2 
sudo systemctl enable apache2

sudo apt-get install -y ganglia-monitor rrdtool gmetad ganglia-webfrontend







