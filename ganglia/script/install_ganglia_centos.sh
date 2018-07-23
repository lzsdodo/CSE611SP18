#!/bin/bash

# Download Ganglia
echo "Installing Ganglia..."

# sudo setenforce 0 # 临时关闭
# sudo vi /etc/selinux/config
# SELINUX=disabled

sudo yum update
sudo yum -y install epel-release
sudo yum -y install httpd rrdtool rrdtool-devel php php-fpm
sudo yum -y install ganglia ganglia-gmond ganglia-gmetad ganglia-web ganglia-gmond-python --enablerepo=epel

sudo mkdir -p /var/lib/ganglia/rrds
sudo mkdir -p /usr/lib/ganglia/python_modules/

sudo chown -R nobody:nobody /var/lib/ganglia/rrds
sudo chown -R nobody:nobody /usr/share/ganglia
sudo chown -R nobody:nobody /usr/lib/ganglia/python_modules/

sudo mv /etc/ganglia/gmetad.conf /etc/ganglia/gmetad.conf.bac
sudo mv /etc/ganglia/gmond.conf /etc/ganglia/gmond.conf.bac

# sudo vi /etc/hosts
# sudo vi /etc/ganglia/gmetad.conf
# sudo vi /etc/ganglia/gmond.conf
# sudo vi /etc/httpd/conf.d/ganglia.conf
# sudo vi /etc/httpd/conf/httpd.conf

# sudo systemctl start gmetad gmond httpd
# sudo systemctl enable gmetad gmond httpd

# sudo firewall-cmd --permanent --zone=public --add-port=8649/udp
# sudo firewall-cmd --permanent --zone=public --add-port=8649-8652/tcp
# sudo firewall-cmd --permanent --zone=public --add-service=ganglia-client
# sudo firewall-cmd --permanent --zone=public --add-service=ganglia-master
# sudo firewall-cmd --reload
