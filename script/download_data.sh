#!/bin/bash

mkdir -p ~/data
cd ~/data


mkdir mnist && cd mnist
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/t10k-images-idx3-ubyte.gz
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/t10k-labels-idx1-ubyte.gz
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/train-images-idx3-ubyte.gz
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/train-labels-idx1-ubyte.gz
cd ~


