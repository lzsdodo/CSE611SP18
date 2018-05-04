#!/bin/bash

wget -c https://github.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/raw/dev/ganglia/script/install_ganglia_master.sh
bash install_ganglia_master.sh

# Start Service
#sudo service gmetad restart
#sudo service ganglia-monitor restart
sudo /etc/init.d/gmetad restart
sudo /etc/init.d/ganglia-monitor restart
sudo /etc/init.d/apache2 restart

