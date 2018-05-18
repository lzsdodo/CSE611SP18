#!/bin/bash

hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<10; i++))
    do
        echo -e "$i time for gan tensorflow\n$(date +%H:%M:%S)" | tee -a record_tf_gan.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./tf_gan.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_tf_gan.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 10s
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<10; i++))
    do
        echo -e "$i time for gan mxnet\n$(date +%H:%M:%S)" | tee -a record_mx_gan.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./mx_gan.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_mx_gan.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 10s
    done

elif [ $hn == "cindy" ]; then
    # Keras
    for ((i=0; i<10; i++))
    do
        echo -e "$i time for gan spk/krs\n$(date +%H:%M:%S)" | tee -a record_mx_spk.txt
        # run code
        cd ~
        cd ./code/gan
        python3 ./krs_gan.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_mx_spk.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 10s
    done
    
fi
