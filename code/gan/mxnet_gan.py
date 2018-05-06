#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_mldata
import numpy as np
import mxnet as mx
import cv2

mnist = fetch_mldata('MNIST original')

np.random.seed(1)
p = np.random.permutation(mnist.data.shape[0])
X = mnist.data[p]
X = X.reshape((70000, 28, 28))

# resize to 64 * 64
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


batch_size = 100
image_iter = mx.io.NDArrayIter(X, batch_size=batch_size)


# Preparing random umbers
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
    
    
Z = 100
rand_iter = RandIter(batch_size, Z)

# Create the Model

## The generator
no_bias = True
fix_gamma = True
epsilon = 1e-5 + 1e-12

rand = mx.sym.Variable('rand')

dense1 = mx.sym.FullyConnected(rand, flatten = True, num_hidden = 512*7*7)
act1 = mx.sym.Activation(dense1, act_type = 'relu')
reshape1 = mx.sym.reshape(act1, shape = (7,7,512))

gbn1 = mx.sym.BatchNorm(rand, name='gbn1', fix_gamma=fix_gamma, eps=epsilon)
gact1 = mx.sym.Activation(gbn1, act_type = 'relu')
gdrop1 = mx.sym.Dropout(gact1, p=0.2)

g2 = mx.sym.Deconvolution(gdrop1, name='g2', kernel=(5,5), stride=(1,1), pad=(2,2), num_filter=256, no_bias=no_bias)
gbn2 = mx.sym.BatchNorm(g2, name='gbn2', fix_gamma=fix_gamma, eps=epsilon)
gact2 = mx.sym.Activation(gbn2, act_type = 'relu')
gdrop2 = mx.sym.Dropout(gact2, p=0.2)

g3 = mx.sym.Deconvolution(gdrop2, name='g3', kernel=(5,5), stride=(2,2), pad=(5,5), num_filter=128, no_bias=no_bias)
gbn3 = mx.sym.BatchNorm(g3, name='gbn3', fix_gamma=fix_gamma, eps=epsilon)
gact3 = mx.sym.Activation(gbn3, act_type = 'relu')
gdrop3 = mx.sym.Dropout(gact3, p=0.2)

g4 = mx.sym.Deconvolution(gact3, name='g4', kernel=(5,5), stride=(2,2), pad=(1,1), num_filter=1, no_bias=no_bias)
generatorSymbol = mx.sym.Activation(g4, name='gact4', act_type='tanh')


## The discriminator
data = mx.sym.Variable('data')

d1 = mx.sym.Convolution(data, name='d1', kernel=(5,5), stride=(2,2), pad=(15,16), num_filter=64, no_bias=no_bias)
dact1 = mx.sym.LeakyReLU(d1, name='dact1', act_type='leaky', slope=0.1)
drop1 = mx.sym.Dropout(dact1, p=0.2)

d2 = mx.sym.Convolution(drop1, name='d2', kernel=(5,5), stride=(2,2), pad=(15,16), num_filter=128, no_bias=no_bias)
dbn2 = mx.sym.BatchNorm(d2, name='dbn2', fix_gamma=fix_gamma, eps=epsilon)
dact2 = mx.sym.LeakyReLU(dbn2, name='dact2', act_type='leaky', slope=0.1)
drop2 = mx.sym.Dropout(dact2, p=0.2)

d3 = mx.sym.Convolution(drop2, name='d3', kernel=(5,5), stride=(2,2), pad=(15,16), num_filter=256, no_bias=no_bias)
dbn3 = mx.sym.BatchNorm(d3, name='dbn3', fix_gamma=fix_gamma, eps=epsilon)
dact3 = mx.sym.LeakyReLU(dbn3, name='dact3', act_type='leaky', slope=0.1)


d5 = mx.sym.Convolution(dact3, name='d5', kernel=(5,5), num_filter=1, no_bias=no_bias)
d5 = mx.sym.Flatten(d5)

label = mx.sym.Variable('label')
discriminatorSymbol = mx.sym.LogisticRegressionOutput(data=d5, label=label, name='dloss')


# Prepare the models using the Module API
#Hyper-parameters
sigma = 0.02
lr = 0.001
beta1 = 0.5
# If you do not have a GPU. Use the below outlined
ctx = mx.gpu() if mx.test_utils.list_gpus() else mx.cpu()

#=============Generator Module=============
generator = mx.mod.Module(symbol=generatorSymbol, data_names=('rand',), label_names=None, context=ctx)
generator.bind(data_shapes=rand_iter.provide_data)
generator.init_params(initializer=mx.init.Normal(sigma))
generator.init_optimizer(
    optimizer='adam',
    optimizer_params={
        'learning_rate': lr,
        'beta1': beta1,
    })
mods = [generator]

# =============Discriminator Module=============
discriminator = mx.mod.Module(symbol=discriminatorSymbol, data_names=('data',), label_names=('label',), context=ctx)
discriminator.bind(data_shapes=image_iter.provide_data,
          label_shapes=[('label', (batch_size,))],
          inputs_need_grad=True)
discriminator.init_params(initializer=mx.init.Normal(sigma))
discriminator.init_optimizer(
    optimizer='adam',
    optimizer_params={
        'learning_rate': lr,
        'beta1': beta1,
    })
mods.append(discriminator)


# Train the model
# =============train===============
print('Training...')
for epoch in range(1):
    image_iter.reset()
    for i, batch in enumerate(image_iter):
        #Get a batch of random numbers to generate an image from the generator
        rbatch = rand_iter.next()
        #Forward pass on training batch
        generator.forward(rbatch, is_train=True)
        #Output of training batch is the 64x64x3 image
        outG = generator.get_outputs()

        #Pass the generated (fake) image through the discriminator, and save the gradient
        #Label (for logistic regression) is an array of 0's since this image is fake
        label = mx.nd.zeros((batch_size,), ctx=ctx)
        #Forward pass on the output of the discriminator network
        discriminator.forward(mx.io.DataBatch(outG, [label]), is_train=True)
        #Do the backward pass and save the gradient
        discriminator.backward()
        gradD = [[grad.copyto(grad.context) for grad in grads] for grads in discriminator._exec_group.grad_arrays]

        #Pass a batch of real images from MNIST through the discriminator
        #Set the label to be an array of 1's because these are the real images
        label[:] = 1
        batch.label = [label]
        #Forward pass on a batch of MNIST images
        discriminator.forward(batch, is_train=True)
        #Do the backward pass and add the saved gradient from the fake images to the gradient
        #generated by this backwards pass on the real images
        discriminator.backward()
        for gradsr, gradsf in zip(discriminator._exec_group.grad_arrays, gradD):
            for gradr, gradf in zip(gradsr, gradsf):
                gradr += gradf
        #Update gradient on the discriminator
        discriminator.update()

        #Now that we've updated the discriminator, let's update the generator
        #First do a forward pass and backwards pass on the newly updated discriminator
        #With the current batch
        discriminator.forward(mx.io.DataBatch(outG, [label]), is_train=True)
        discriminator.backward()
        #Get the input gradient from the backwards pass on the discriminator,
        #and use it to do the backwards pass on the generator
        diffD = discriminator.get_input_grads()
        generator.backward(diffD)
        #Update the gradients on the generator
        generator.update()

        #Increment to the next batch, printing every 50 batches
        i += 1
        if i % 50 == 0:
            print('epoch:', epoch, 'iter:', i)
            print
            print("   From generator:        From MNIST:")

