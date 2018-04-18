#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:00:16 2018

@author: keyspan
"""

from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("LinearRegression")\
    .getOrCreate()

# Load training data
### !!! PROBLEM START
training = spark.read.format("libsvm").load("/Users/py/Python/Python3.6/dodo_574/proj2/sample_linear_regression_data.txt")
### !!! PROBLEM END

lr = LinearRegression(maxIter=10)

# Fit the model
lrModel = lr.fit(training)

# Print the coefficients and intercept for linear regression
print("Coefficients: %s" % str(lrModel.coefficients))
print("Intercept: %s" % str(lrModel.intercept))

# Summarize the model over the training set and print out some metrics
trainingSummary = lrModel.summary
print("numIterations: %d" % trainingSummary.totalIterations)
print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))
trainingSummary.residuals.show()
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)

spark.stop()