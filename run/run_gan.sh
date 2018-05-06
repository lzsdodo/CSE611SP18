#!/bin/bash

hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<10; i++))
    do
        echo "$i time for gan tensorflow" | tee -a record_tf_gan.txt
        date | tee -a record_tf_gan.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./tf_gan.py
        cd ~
        echo "Completed" | tee -a record_tf_gan.txt
        date | tee -a record_tf_gan.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<10; i++))
    do
        echo "$i time for gan mxnet" | tee -a record_mx_gan.txt
        date | tee -a record_mx_gan.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./mx_gan.py
        cd ~
        echo "Completed" | tee -a record_mx_gan.txt
        date | tee -a record_mx_gan.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done
    
fi
