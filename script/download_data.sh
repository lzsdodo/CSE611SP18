#!/bin/bash

creditcard_data=1wn72YO8sBNtUpnlbrdxOWb5d3X08VT3Q
mnist_data=1E3n3zlznb5J8zchG0L6gSkF4E2m_k4Wl

wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/script/gdlink.sh
mv ./gdlink.sh ./gdlink
sudo chmod a+x ./gdlink

./gdlink ${creditcard_data} | xargs -n1 wget -c -O ./data/creditcard.csv
./gdlink ${mnist_data} | xargs -n1 wget -c -O ./data/mnist_jpg.zip
unzip ./data/mnist_jpg.zip -d ./data/
mv ./data/mnist ./data/mnist_jpg
rm ./data/mnist_jpg.zip

