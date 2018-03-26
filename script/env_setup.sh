#!/bin/bash

wget -c https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

sudo apt-get update
sudo apt-get install python python-dev python3 python3-dev
python pip install --upgrade pip