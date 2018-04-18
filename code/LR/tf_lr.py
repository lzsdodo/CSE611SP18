#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:20:46 2018

@author: keyspan
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

learning_rate = 0.01
steps = 100
ck_steps = 10

train_data = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])

train_label = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])

sample_size = len(train_data)
feature_size = 1

# Construct graph on tensorflow
X = tf.placeholder(tf.float32, [sample_size,])
y = tf.placeholder(tf.float32, [sample_size,])

w = tf.get_variable('weight', [feature_size])
b = tf.get_variable('bias', [feature_size])

pred = tf.add(tf.multiply(X,w), b)

cost = tf.reduce_mean(tf.pow(pred - y, 2))

opt = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    for step in range(steps):
        X_batch, y_batch = (train_data, train_label)
        _, costs = sess.run([opt,cost], feed_dict = {X: X_batch, y: y_batch})
        
        if (step + 1) % ck_steps == 0:
            print('Step:', step, "cost is", costs)
    
    plt.plot(train_data, train_label, 'ro', label='True data')
    plt.plot(train_data, train_data*w.eval() + b.eval(), label='Fitted data')
    plt.legend()
    plt.show()