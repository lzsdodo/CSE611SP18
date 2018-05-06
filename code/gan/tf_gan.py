#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from glob import glob
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot
import doutils
import tensorflow as tf
import helper
from datetime import datetime
from ft_notify import send_to_channel

show_n_images = 20
mnist_images = doutils.get_batch(glob(os.path.join('../../data', 'mnist_jpg/*.jpg'))[:show_n_images], 28, 28, 'L')

def model_inputs(image_width, image_height, image_channels, z_dim):
    
    inputs_real = tf.placeholder(tf.float32, (None, image_width, image_height, image_channels), name='input_real')
    inputs_z = tf.placeholder(tf.float32, (None, z_dim), name='input_z')
    learning_rate = tf.placeholder(tf.float32, (), name="learning_rate")
    return inputs_real, inputs_z, learning_rate

def discriminator(images, reuse=False):
    alpha = 0.1;
    with tf.variable_scope('discriminator', reuse=reuse):
        x1 = tf.layers.conv2d(images, 64, 5, strides=2, padding='same', kernel_initializer=tf.contrib.layers.xavier_initializer())
        relu1 = tf.maximum(alpha * x1, x1)
        dropout1 = tf.nn.dropout(relu1, .8)
        
        x2 = tf.layers.conv2d(dropout1, 128, 5, strides=2, padding='same', kernel_initializer=tf.contrib.layers.xavier_initializer())
        bn2 = tf.layers.batch_normalization(x2, training=True)
        relu2 = tf.maximum(alpha * bn2, bn2)
        dropout2 = tf.nn.dropout(relu2, .8)
        
        x3 = tf.layers.conv2d(dropout2, 256, 5, strides=2, padding='same', kernel_initializer=tf.contrib.layers.xavier_initializer())
        bn3 = tf.layers.batch_normalization(x3, training=True)
        relu3 = tf.maximum(alpha * bn3, bn3)
        dropout3 = tf.nn.dropout(relu3, .8)
        
        flat = tf.reshape(dropout3, (-1, 4*4*256))
        logits = tf.layers.dense(flat, 1)
        out = tf.sigmoid(logits)
    
    return out, logits

def generator(z, out_channel_dim, is_train=True):
    alpha = 0.1
    
    with tf.variable_scope('generator', reuse=not is_train):
        x1 = tf.layers.dense(z, 7*7*512)
        x1 = tf.reshape(x1, (-1, 7, 7, 512))
        bn1 = tf.layers.batch_normalization(x1, training=is_train)
        relu1 = tf.maximum(alpha * bn1, bn1)
        dropout1 = tf.nn.dropout(relu1, .8) # x7x512
        x2 = tf.layers.conv2d_transpose(dropout1, 256, 5, strides=1, padding='same', kernel_initializer=tf.contrib.layers.xavier_initializer())
        bn2 = tf.layers.batch_normalization(x2, training=is_train)
        relu2 = tf.maximum(alpha * bn2, bn2)
        dropout2 = tf.nn.dropout(relu2, .8) # 14x14x256
        x3 = tf.layers.conv2d_transpose(dropout2, 128, 5, strides=2, padding='same', kernel_initializer=tf.contrib.layers.xavier_initializer())
        bn3 = tf.layers.batch_normalization(x3, training=is_train)
        relu3 = tf.maximum(alpha * bn3, bn3)
        dropout3 = tf.nn.dropout(relu3, .8)
        
        
        logits = tf.layers.conv2d_transpose(dropout3, out_channel_dim, 5, strides=2, padding='same', kernel_initializer=tf.contrib.layers.xavier_initializer())
        # 28 x 28 x out_channel_dim images.
    return tf.tanh(logits)

def model_loss(input_real, input_z, out_channel_dim):
    g_model = generator(input_z, out_channel_dim)
    d_model_real, d_logits_real = discriminator(input_real)
    d_model_fake, d_logits_fake = discriminator(g_model, reuse=True)
    
    d_loss_real = tf.reduce_mean(
        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_real, labels=tf.ones_like(d_model_real)*.9)
    )
    d_loss_fake = tf.reduce_mean(
        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake, labels=tf.zeros_like(d_model_fake))
    )
    g_loss = tf.reduce_mean(
        tf.nn.sigmoid_cross_entropy_with_logits(logits=d_logits_fake, labels=tf.ones_like(d_model_fake))
    )
    d_loss = d_loss_real + d_loss_fake
    
    return d_loss, g_loss

def model_opt(d_loss, g_loss, learning_rate, beta1):
    t_vars = tf.trainable_variables()
    d_vars = [var for var in t_vars if var.name.startswith('discriminator')]
    g_vars = [var for var in t_vars if var.name.startswith('generator')]
    
    with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
        d_train_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(d_loss, var_list=d_vars)
        g_train_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(g_loss, var_list=g_vars)
        
    return d_train_opt, g_train_opt

import numpy as np

def show_generator_output(sess, n_images, input_z, out_channel_dim, image_mode, step):
    cmap = None if image_mode == 'RGB' else 'gray'
    z_dim = input_z.get_shape().as_list()[-1]
    example_z = np.random.uniform(-1, 1, size=[n_images, z_dim])

    samples = sess.run(
        generator(input_z, out_channel_dim, False),
        feed_dict={input_z: example_z})

    images_grid = doutils.images_square_grid(samples, image_mode)
    pyplot.imshow(images_grid, cmap=cmap)
    pyplot.savefig("./images/tf/mnist_%d.png" % step)
    pyplot.show()
    
    
def train(epoch_count, batch_size, z_dim, learning_rate, beta1, get_batches, data_shape, data_image_mode):
    _, image_width, image_height, num_channels = data_shape
    input_real, input_z, learning_rate_input = model_inputs(image_width, image_height, num_channels, z_dim)
    d_loss, g_loss = model_loss(input_real, input_z, num_channels)
    d_opt, g_opt = model_opt(d_loss, g_loss, learning_rate, beta1)
    
    steps = 0
    show_every = 100
    print_every = 20
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        starttime = datetime.now()
        for epoch_i in range(epoch_count):
            for batch_images in get_batches(batch_size):
                # TODO: Train Model
                steps += 1
                batch_z = np.random.uniform(-1, 1, size=(batch_size, z_dim))
                batch_images = batch_images * 2
                _ = sess.run(d_opt, feed_dict={input_real: batch_images, input_z: batch_z, learning_rate_input: learning_rate})
                _ = sess.run(g_opt, feed_dict={input_real: batch_images, input_z: batch_z, learning_rate_input: learning_rate})
                if steps % show_every == 0:
                    show_generator_output(sess, 64, input_z, num_channels, data_image_mode, steps)
                
                if steps % print_every == 0:
                    train_loss_d = d_loss.eval({input_real: batch_images, input_z: batch_z})
                    train_loss_g = g_loss.eval({input_z: batch_z})
                    
                    print('Step: {}'.format(steps),
                         'Epoch {}/{}...'.format(epoch_i, epoch_count),
                         'Discriminator Loss: {:.4f}...'.format(train_loss_d),
                         'Generator Loss: {:.4f}...'.format(train_loss_g)) 
                    
                    
        print('Training time for 2 epoch is ',(datetime.now()-starttime).seconds)
                    
def main():                   
    batch_size = 100
    z_dim = 100
    learning_rate = 0.001
    beta1 = 0.5
    epochs = 2
    
    mnist_dataset = doutils.Dataset('mnist', glob(os.path.join(data_dir, 'mnist/*.jpg')))
    with tf.Graph().as_default():
        send_to_channel(channel_api, sendkey, 'gan-gan-tf', 'Training starts!')
        train(epochs, batch_size, z_dim, learning_rate, beta1, mnist_dataset.get_batches,
              mnist_dataset.shape, mnist_dataset.image_mode)
        send_to_channel(channel_api, sendkey, 'gan-gan-tf', 'Congrats! Completed')
        
# Training time for 2 epoch is  13314
        
if __name__ == '__main__':
    main()