#!/bin/bash

cd ~
mkdir code script data
mkdir -p code/gan/images/mxnet
mkdir -p code/gan/images/tf

# For System
## Set Timezone
#timedatectl list-timezones
sudo timedatectl set-timezone America/New_York

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y build-essential libpq-dev libssl-dev libffi-dev openssl zlib1g-dev libbz2-dev pkg-config zip g++ unzip git

# Setup ENV
hn=$(hostname)
echo "$hn node"

if [ $hn == "master" ]; then
    # Master

    # Ganglia
    wget -c https://raw.githubusercontent.com/lzsdodo/CSE611SP18/master/ganglia/script/install_ganglia_master.sh
    bash install_ganglia_master.sh
    # Start Service
    #sudo service gmetad restart
    #sudo service ganglia-monitor restart
    sudo /etc/init.d/gmetad restart
    sudo /etc/init.d/apache2 restart


elif [ $hn == "ann" ]; then
    # Tensorflow

    # Ganglia
    wget -c https://raw.githubusercontent.com/lzsdodo/CSE611SP18/master/ganglia/script/install_ganglia_client.sh
    bash install_ganglia_client.sh
    rm install_ganglia_client.sh

elif [ $hn == "bob" ]; then
    # MXNet

    # Ganglia
    wget -c https://raw.githubusercontent.com/lzsdodo/CSE611SP18/master/ganglia/script/install_ganglia_client.sh
    bash install_ganglia_client.sh
    rm install_ganglia_client.sh


elif [ $hn == "cindy" ]; then
    # Spark

    # Ganglia
    wget -c https://raw.githubusercontent.com/lzsdodo/CSE611SP18/master/ganglia/script/install_ganglia_client.sh
    bash install_ganglia_client.sh
    rm install_ganglia_client.sh


    # Java for Spark
    sudo apt-get install -y default-jre default-jdk
    sudo add-apt-repository ppa:webupd8team/java
    sudo apt-get update -y
    sudo apt-get install -y oracle-java8-installer
    sudo update-alternatives --config java
    #0
    echo 'JAVA_HOME="/usr/lib/jvm/java-8-oracle"' | sudo tee -a /etc/environment
    source /etc/environment
    echo $JAVA_HOME


else
    echo "Unknown hostname."
fi

echo "Completed congiguration for $hn."


# Download Data
echo "Downloading data..."
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611SP18/master/script/download_data.sh
bash download_data.sh
rm download_data.sh
rm gdlink

sudo /etc/init.d/ganglia-monitor restart
