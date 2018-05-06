# Dataset
## LR: Credit Card Fraud Detection on Kaggle
> [Dataset: Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud/data)		 

## Image Classification / Gans: Handwritten digits classification 
> [Dataset: MNIST](http://yann.lecun.com/exdb/mnist/)				


# Hyper-Parameters

## Logistic Regression:

1. learning_rate = 0.1
2. batch_size = 100

## Image Classification

1. batch_size = 100
2. learning_rate = 0.1
3. First Layer = 128
4. Second Layer = 64
5. Third Layer = 10

## GANs

- Discriminator
    1. Conv2d: Filters: 64 Kernel size: 5 Stride: 2 padding: same
    2. Relu: alpha : 0.1
    3. Dropout: drop rate: 0.2
    4. Conv2d: Filters: 128 Kernel size: 5 Stride: 2 padding: same
    5. Batch Normalization
    6. Relu: alpha: 0.1
    7. Dropout: rate: 0.2
    8. Conv2d: Filters: 256 Kernel size: 5 Stride: 2 padding: same
    9. Batch Normalization
    10. Relu: alpha : 0.1
    11. Flatten: (-1, 4*4*256)

- Generator
    1. Dense: 7*7*512
    2. Batch normalization
    3. Relu: alpha = 0.1
    4. Dropout: 0.2
    5. deconv ﬁlter = 256, output size = 5, stride = 1, padding = same
    6. Batch normalization
    7. Relu: alpha = 0.1
    8. Dropout: 0.2
    9. deconv ﬁlter = 128, output size = 5, stride = 2, padding = same
    10. Batch normalization
    11. Relu: 0.1
    12. Dropout: 0.2
    13. deconv: outchannel size = 28 x 28*(3), output size = 5, stride = 2, padding = same
    14. Tanh

- others
    1. batch_size = 100
    2. z = 100
    3. learning rate = 0.01