#!/bin/bash

# Download Ganglia
echo "Installing Ganglia..."
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install -y rrdtool ganglia-monitor gmetad ganglia-webfrontend ganglia-monitor-python


# Configure Ganglia
echo "Configuring apache, rrds and python modules..."
sudo cp /etc/ganglia-webfrontend/apache.conf /etc/apache2/sites-enabled/ganglia.conf
sudo mkdir -p /var/lib/ganglia/rrds
sudo mkdir -p /usr/lib/ganglia/python_modules/
sudo ln -s /usr/share/ganglia-webfrontend/ /var/www/ganglia
sudo chown nobody:nogroup /var/lib/ganglia/rrds
sudo chown nobody:nogroup /usr/lib/ganglia/python_modules/
sudo chown nobody:nogroup /var/www/ganglia

echo "Configuring host, gmetad and gmond"
# Move Configuration Files
sudo mv /etc/ganglia/gmetad.conf /etc/ganglia/gmetad.conf.bac
sudo mv /etc/ganglia/gmond.conf /etc/ganglia/gmond.conf.bac

wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/hosts.conf
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/gmetad.conf
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/gmond.conf
wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/ganglia/conf/conf.d/multicpu.conf

cat ./hosts.conf | sudo tee -a /etc/hosts
sudo mv ./gmetad.conf /etc/ganglia/gmetad.conf
sudo mv ./gmond.conf /etc/ganglia/gmond.conf
sudo mv ./multicpu.conf /etc/ganglia/conf.d/multicpu.conf

