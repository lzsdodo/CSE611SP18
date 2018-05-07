#!/bin/bash

hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<10; i++))
    do
        echo -e "$i time for ic tensorflow\n$(date +%H:%M:%S)" | tee -a record_tf_ic.txt
        # run code
        cd ~
        cd ./code/ic
        python3 ./tf_ic.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_tf_ic.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 10s
        
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<5; i++))
    do
        echo -e "$i time for ic mxnet\n$(date +%H:%M:%S)" | tee -a record_mx_ic.txt
        # run code
        cd ~
        cd ./code/ic
        python3 ./mx_ic.py
        cd ~
        echo -e "$(date +%H:%M:%S)\nCompleted" | tee -a record_mx_ic.txt
        sync; echo 3 | sudo tee /proc/sys/vm/drop_caches
        sleep 10s
    done

fi
