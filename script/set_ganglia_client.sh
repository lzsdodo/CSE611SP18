#!/bin/bash

wget -c https://github.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/raw/dev/ganglia/script/install_ganglia_client.sh
bash install_ganglia_client.sh


# Start Service
sudo /etc/init.d/ganglia-monitor restart
#sudo service ganglia-monitor restart