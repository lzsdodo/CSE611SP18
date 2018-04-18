#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:58:40 2018

@author: keyspan
"""

# Reference tutorial: https://mxnet.incubator.apache.org/tutorials/python/linear-regression.html

import mxnet as mx
import numpy as np
import graphviz

# preparing the data
train_data = np.random.uniform(0, 1, [100, 2])
train_label = np.array([train_data[i][0] + 2 * train_data[i][1] for i in range(100)])
batch_size = 1

# evaluation data
eval_data = np.array([[7,2],[6,10], [12,2]])
eval_label = np.array([11,25,16])


# preparing the data2
train_data = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])

train_label = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
batch_size = 1

# evaluation data2
eval_data = np.array([1, 2, 3, 4])
eval_label = np.array([0.5, 1, 1.5, 2])

# NDArrayIter, which is useful for iterating over both numpy ndarrays and MXNet NDArrays.
train_iter = mx.io.NDArrayIter(train_data, train_label, batch_size, shuffle = True, label_name = 'lr_label')
eval_iter = mx.io.NDArrayIter(eval_data, eval_label, batch_size, shuffle = False)

# Defining the Model:
X = mx.sym.Variable('data')
Y = mx.sym.Variable('lr_label')
# The fully connected symbol represents a fully connected layer of neural network
# (without any activation being applied).
fully_connected_layer = mx.sym.FullyConnected(data = X, name = 'fc1', num_hidden = 1)
# LinearRegressionOutput layer computes the l2 loss against its input and the labels 
# provided to it.
lro = mx.sym.LinearRegressionOutput(data = fully_connected_layer, label = Y, name = 'lro')

model = mx.mod.Module(symbol = lro, 
                      data_names = ['data'],
                      label_names = ['lr_label'])   
# Notice: the label_names must match the train_iter label_name and Y(symbol) label_name

mx.viz.plot_network(symbol = lro)

# Training the model
model.fit(train_iter, eval_iter,
          optimizer_params = {'learning_rate': 0.005, 'momentum': 0.9},
          num_epoch = 20,
          eval_metric = 'mse',
          batch_end_callback = mx.callback.Speedometer(batch_size, 2))

# Using a trained model(Testing and Inference)
model.predict(eval_iter).asnumpy()
# Or choose some metric to evaluate
metric = mx.metric.MSE()
model.score(eval_iter, metric)