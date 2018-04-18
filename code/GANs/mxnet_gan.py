#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:22:01 2018

@author: py
"""

from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')

import numpy as np
np.random.seed(1)
p = np.random.permutation(mnist.data.shape[0])
X = mnist.data[p]
X = X.reshape((70000, 28, 28))

# resize to 64 * 64
import cv2
X = np.asarray([cv2.resize(x, (64,64)) for x in X])

# rerange between -1 and 1
X = X.astype(np.float32)/(255.0/2) - 1.0

# We need to add 3 channels to the images.  
# Since the MNIST dataset is grayscale, 
# we only need 1 channel to represent the dataset. 
# We will pad the other channels with 0’s:
X = X.reshape((70000, 1, 64, 64))
X = np.tile(X, (1, 3, 1, 1))

# put the images into MXNet’s NDArrayIter, 
# which will allow MXNet to easily iterate through the images during training
import mxnet as mx
batch_size = 64
image_iter = mx.io.NDArrayIter(X, batch_size=batch_size)


# Preparing random numbers
class RandIter(mx.io.DataIter):
    def __init__(self, batch_size, ndim):
        self.batch_size = batch_size
        self.ndim = ndim
        self.provide_data = [('rand', (batch_size, ndim, 1, 1))]
        self.provide_label = []

    def iter_next(self):
        return True

    def getdata(self):
        #Returns random numbers from a gaussian (normal) distribution
        #with mean=0 and standard deviation = 1
        return [mx.random.normal(0, 1.0, shape=(self.batch_size, self.ndim, 1, 1))]