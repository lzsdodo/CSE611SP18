#!/bin/bash
 
hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<20; i++))
    do
        echo "$i time for lr tensorflow" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/lr
        python3 ./tf_lr.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<20; i++))
    do
        echo "$i time for lr mxnet" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/lr
        python3 ./mx_lr.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done
    
    
elif [ $hn == "cindy" ]; then
    # Spark
    for ((i=0; i<20; i++))
    do
        echo "$i time for lr spark" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/lr
        python3 ./spk_lr.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done

fi



