#!/bin/bash
 
hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<20; i++))
    do
        echo -e "$i time for lr tensorflow\n$(date +%H:%M:%S)" | tee -a record_tf_lr.txt
        # run code
        cd ~
        cd ./code/lr
        python3 ./tf_lr.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_tf_lr.txt
        date | tee -a record_tf_lr.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<20; i++))
    do
        echo -e "$i time for lr mxnet\n$(date +%H:%M:%S)" | tee -a record_mx_lr.txt
        # run code
        cd ~
        cd ./code/lr
        python3 ./mx_lr.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_mx_lr.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done
    
    
elif [ $hn == "cindy" ]; then
    # Spark
    for ((i=0; i<20; i++))
    do
        echo -e "$i time for lr spark\n$(date +%H:%M:%S)" | tee -a record_spk_lr.txt
        # run code
        cd ~
        cd ./code/lr
        python3 ./spk_lr.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_spk_lr.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 2m
    done

fi



