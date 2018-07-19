#!/bin/bash

# Download Ganglia
echo "Installing Ganglia..."

sudo yum update && yum -y install epel-release

sudo yum -y install rrdtool
sudo yum -y install ganglia ganglia-gmond ganglia-gmetad ganglia-web --enablerepo=epel


sudo mkdir -p /var/lib/ganglia/rrds
sudo mkdir -p /usr/lib/ganglia/python_modules/
sudo ln -s /usr/share/ganglia/ /var/www/html/ganglia

sudo chown nobody:nobody /var/lib/ganglia/rrds
sudo chown nobody:nobody /usr/lib/ganglia/python_modules/
sudo chown nobody:nobody /var/www/html/ganglia

sudo mv /etc/ganglia/gmetad.conf /etc/ganglia/gmetad.conf.bac
sudo mv /etc/ganglia/gmond.conf /etc/ganglia/gmond.conf.bac

# vi /etc/ganglia/gmetad.conf
# vi /etc/ganglia/gmond.conf

# vi /etc/httpd/conf/httpd.conf
# DocumentRoot "/var/www/html"

# vi /etc/httpd/conf.d/ganglia.conf

# firewall-cmd --add-port=8649/udp --permanent
# setsebool -P httpd_can_network_connect 1

# systemctl restart httpd gmetad gmond
# systemctl enable httpd gmetad httpd
