#!/bin/bash

sudo apt-get -y update && sudo apt-get -y upgrade

# For Ganglia
## Ganglia Client 
sudo apt-get install -y ganglia-monitor

## Ganglia Master Node
## Install LAMP on your server
sudo apt-get install -y apache2 php libapache2-mod-php 

sudo ln -s /usr/share/ganglia-webfrontend/ /var/www/ganglia
sudo systemctl start apache2 
sudo systemctl enable apache2

sudo apt-get install -y rrdtool ganglia-monitor gmetad ganglia-webfrontend

sudo mkdir -p /var/lib/ganglia/rrds
sudo chown nobody:nobody /var/lib/ganglia/rrds
chmod a+w /var/lib/ganglia/rrds
sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf