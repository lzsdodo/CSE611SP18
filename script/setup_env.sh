#!/bin/bash

cd ~ && mkdir script code data


# For System
## Set Timezone
#timedatectl list-timezones
sudo timedatectl set-timezone America/New_York

sudo apt-get -y update && sudo apt-get -y upgrade
sudo apt-get install -y build-essential libpq-dev libssl-dev libffi-dev openssl zlib1g-dev
sudo apt-get install -y pkg-config zip g++ unzip

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













