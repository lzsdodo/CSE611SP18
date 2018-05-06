#!/bin/bash

#!/bin/bash
 
hn=$(hostname)
echo "$hn node"

if [ $hn == "ann" ]; then
    # Tensorflow
    for ((i=0; i<10; i++))
    do
        echo "$i time for ic tensorflow" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/ic
        python3 ./tf_ic.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sleep 2m
    done

elif [ $hn == "bob" ]; then
    # MXNet
    for ((i=0; i<10; i++))
    do
        echo "$i time for ic mxnet" | tee -a record.txt
        date | tee -a record.txt
        # run code
        cd ~
        cd ./code/ic
        python3 ./mx_ic.py
        cd ~
        echo "Completed" | tee -a record.txt
        date | tee -a record.txt
        sleep 2m
    done
    
    
elif [ $hn == "cindy" ]; then
    # Spark

fi



