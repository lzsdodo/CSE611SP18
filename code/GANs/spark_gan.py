#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyspark.ml.classification import MultilayerPerceptronClassifier
data = spark.read.format("libsvm").load("data/mllib/sample_multiclass_classification_data.txt")