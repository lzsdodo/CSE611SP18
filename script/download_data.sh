#!/bin/bash

cd ~
mkdir data
cd ./data

mkdir kaggle
cd kaggle
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/kaggle/sampleSubmission.csv
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/kaggle/test.csv
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/kaggle/train.csv
cd ..

mkdir mnist
cd mnist
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/t10k-images-idx3-ubyte.gz
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/t10k-labels-idx1-ubyte.gz
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/train-images-idx3-ubyte.gz
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/mnist/train-labels-idx1-ubyte.gz
# Unzip 
cd ..

mkdir celeba
cd celeba
# Download
# Unzip
# Remove trash
cd ..

mkdir gutenberg
cd gutenberg
wget -c https://github.com/lzsdodo/Ganglia_Monitoring_in_GCP/blob/master/data/gutenberg/WinstonChurchill.txt.zip
unzip 
# Unzip
# Remove trash
cd ..