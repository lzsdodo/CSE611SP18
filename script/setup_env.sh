#!/bin/bash

cd ~ && mkdir script code data


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













