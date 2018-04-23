#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import pandas as pd

learning_rate = 1
steps = 20000
ck_steps = 1000

data_pd = pd.read_csv("../data/lr/iris.txt",
                          header = None, sep = ',', names = ['x1', 'x2', 'x3', 'x4', 'y'])
# transform categorical variable
data_pd = pd.get_dummies(data_pd)

# split into train and test data
np.random.seed(1)
msk = np.random.rand(len(data_pd)) < 0.8
train_data = data_pd[msk].iloc[:,0:4].as_matrix()
train_label = data_pd[msk].iloc[:,4:].as_matrix()
test_data = data_pd[~msk].iloc[:,0:4].as_matrix()
test_label = data_pd[~msk].iloc[:, 4:].as_matrix()

sample_size = train_data.shape[0]
feature_size = train_data.shape[1]
class_size = train_label.shape[1]

tf.reset_default_graph()
# Construct graph on tensorflow
X = tf.placeholder(tf.float32, [None,feature_size])
y = tf.placeholder(tf.float32, [None, class_size])

w = tf.get_variable('weight', shape = [feature_size,class_size], initializer = tf.random_normal_initializer())
b = tf.get_variable('bias', shape = [class_size], initializer = tf.zeros_initializer())

y_hat =  tf.nn.softmax(tf.add(tf.matmul(X,w), b))

pred = tf.argmax(y_hat, axis = 1)

y_label = tf.argmax(y, axis = 1)

accuracy = tf.reduce_mean(tf.cast(tf.equal(pred, y_label), tf.float32))

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y, logits = y_hat))

opt = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    cost_ave = 0
    for step in range(steps):
        X_batch, y_batch = (train_data, train_label)
        _, costs = sess.run([opt,cost], feed_dict = {X: X_batch, y: y_batch})
        cost_ave += costs/ck_steps
        if (step + 1) % ck_steps == 0:
            print('Step:', step, "cost is", cost_ave)
            cost_ave = 0
    t_accuracy= sess.run(accuracy, feed_dict = {X: train_data, y: train_label})
    print('The train accuracy is', t_accuracy)
    te_accuracy= sess.run(accuracy, feed_dict = {X: test_data, y: test_label})
    print('The test accuracy is', te_accuracy)