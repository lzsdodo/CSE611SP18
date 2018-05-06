#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reference tutorial: https://mxnet.incubator.apache.org/tutorials/python/linear-regression.html

import mxnet as mx
import numpy as np
import pandas as pd

data_pd = pd.read_csv("../../data/kaggle/creditcard.csv", sep = ',')
# transform categorical variable
data_pd = pd.get_dummies(data_pd, columns = ['Class'])

# split into train and test data
np.random.seed(1)
msk = np.random.rand(len(data_pd)) < 0.8
train_data = data_pd[msk].iloc[:,0:30].as_matrix()
train_label = data_pd[msk].iloc[:,30:].as_matrix()
test_data = data_pd[~msk].iloc[:,0:30].as_matrix()
test_label = data_pd[~msk].iloc[:, 30:].as_matrix()

batch_size = 100

# NDArrayIter, which is useful for iterating over both numpy ndarrays and MXNet NDArrays.
train_iter = mx.io.NDArrayIter(train_data, train_label, batch_size, shuffle = True, label_name = 'lr_label')
test_iter = mx.io.NDArrayIter(test_data, test_label, batch_size, shuffle = False)

# Defining the Model:
X = mx.sym.Variable('data')
Y = mx.sym.Variable('lr_label')
# The fully connected symbol represents a fully connected layer of neural network
# (without any activation being applied).
fully_connected_layer = mx.sym.FullyConnected(data = X, name = 'fc1', num_hidden = 2)
# LinearRegressionOutput layer computes the l2 loss against its input and the labels 
# provided to it.
lro = mx.sym.LogisticRegressionOutput(data = fully_connected_layer, label = Y, name = 'lro')

model = mx.mod.Module(symbol = lro, 
                      data_names = ['data'],
                      label_names = ['lr_label'])   

# Training the model
model.fit(train_iter,num_epoch = 100)

# Using a trained model(Testing and Inference)
predictions = np.argmax(model.predict(test_iter).asnumpy(), axis = 1)
accuracy = np.mean(predictions == np.argmax(test_label, axis = 1))
print('The test accuracy is', accuracy)
