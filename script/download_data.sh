#!/bin/bash

wget -c https://raw.githubusercontent.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/dev/script/gdlink.sh -O ./gdlink
sudo chmod a+x gdlink

creditcard_data=1wn72YO8sBNtUpnlbrdxOWb5d3X08VT3Q
mkdir -p ./data/kaggle
./gdlink ${creditcard_data} | xargs -n1 wget -c -O ./data/kaggle/creditcard.csv


mkdir -p ./data/mnist && cd ./data/mnist
wget -c https://github.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/raw/dev/data/mnist/t10k-images-idx3-ubyte.gz
wget -c https://github.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/raw/dev/data/mnist/t10k-labels-idx1-ubyte.gz
wget -c https://github.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/raw/dev/data/mnist/train-images-idx3-ubyte.gz
wget -c https://github.com/lzsdodo/CSE611_Ganglia_Monitoring_in_GCP/raw/dev/data/mnist/train-labels-idx1-ubyte.gz
cd ~

mnist_data=1jyatVgDSnBafdfoz4LVhczqpfxvsc6mw
./gdlink ${mnist_data} | xargs -n1 wget -c -O ./data/mnist/jpg.zip
unzip ./data/mnist/jpg.zip -d ./data/mnist
rm ./data/mnist/jpg.zip

rm gdlink
