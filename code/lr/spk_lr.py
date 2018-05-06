#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
#from pyspark.sql.types import StructType, StructField
#from pyspark.sql.types import DoubleType, StringType
from pyspark.ml.feature import VectorAssembler
import pandas as pd
import numpy as np
from sklearn.utils import resample

spark = SparkSession.builder.appName("LogisticRegression").getOrCreate()

#schema = StructType([StructField('x1', DoubleType()), StructField('x2', DoubleType()), 
#                     StructField('x3', DoubleType()), StructField('x4', DoubleType()),
#                     StructField('y', StringType())])
# Load training data
#training = spark.read.csv("/Users/keyspan/Documents/zachary/cse611/data/classification/iris.txt",
#                          header = False, sep = ',', schema = schema)
    
# read data using pandas
data_pd = pd.read_csv("../../data/kaggle/creditcard.csv", sep = ',')

# transform categorical variable
#data_pd.Class = pd.Categorical(data_pd.Class)
#data_pd['Class'] = data_pd.Class.cat.codes

ordered_data = data_pd['Class'].values.reshape(-1,1)
data_pd = pd.DataFrame(np.hstack((ordered_data, data_pd.loc[:,'Time':'Amount'])))
feature_names = ['label'] + ['f' + str(x) for x in range(30)]
data_pd.columns = feature_names

# split into train and test data
np.random.seed(1)
msk = np.random.rand(len(data_pd)) < 0.6
train_pd = data_pd[msk]
test_pd = data_pd[~msk]


# create dataframe in pyspark
train = spark.createDataFrame(train_pd)
test = spark.createDataFrame(test_pd)
assembler = VectorAssembler(inputCols = feature_names[1:],
                            outputCol = 'features')
train_assemble = assembler.transform(train).select('label', 'features')
test_assemble = assembler.transform(test).select('label', 'features')
# Build and fit the model
lr = LogisticRegression(maxIter=100, regParam = 0.3, elasticNetParam = 0.8)
lrModel = lr.fit(train_assemble)

# Accuracy
predictions = lrModel.transform(train_assemble).select('prediction').head(len(train_pd))
predictions_list = np.array([int(x.prediction) for x in predictions])
accuracy = np.mean(predictions_list == np.array(train_pd['label']))
print('The training accuracy is ', accuracy)

predictions = lrModel.transform(test_assemble).select('prediction').head(len(data_pd))
predictions_list = [int(x.prediction) for x in predictions]
accuracy = np.mean(predictions_list == test_pd['label'])
print('The test accuracy is ', accuracy)

spark.stop()
