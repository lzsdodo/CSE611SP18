#!/bin/bash

hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<10; i++))
    do
        echo "$i time for gan tensorflow" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./tf_gan.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sleep 2m
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<10; i++))
    do
        echo "$i time for gan mxnet" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./mx_gan.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sleep 2m
    done
    
fi
