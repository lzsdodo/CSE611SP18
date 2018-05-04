#!/bin/bash

# Download Ganglia
echo "Installing Ganglia..."
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y ganglia-monitor ganglia-monitor-python

echo "Installing python modules..."
sudo mkdir -p /usr/lib/ganglia/python_modules/
sudo chown nobody:nogroup /usr/lib/ganglia/python_modules/

echo "Configuring host and gmond"
# Move Configuration Files
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/hosts.conf
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/gmond.conf
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/conf.d/multicpu.conf

cat ./hosts.conf | sudo tee -a /etc/hosts
sudo mv /etc/ganglia/gmond.conf /etc/ganglia/gmond.conf.bac
sudo mv ./gmond.conf /etc/ganglia/gmond.conf
sudo mv ./multicpu.conf /etc/ganglia/conf.d/multicpu.conf
