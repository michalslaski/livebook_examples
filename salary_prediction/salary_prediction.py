# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import tensorflow as tf
import time;

# columns = ['year','inflation','pl_salary']
data = pd.read_csv('salaries.csv', header=None).values

# make it a 2D array of size N x D where D = 1
X = data[:,0].reshape(-1, 1)

# center inputs around 0
X = X - 2015

# prepare training data
Y = data[:,2]
Y = np.log(Y)

start = time.time()

# create model
model = tf.keras.models.Sequential(
    [tf.keras.layers.InputLayer(input_shape=(1,)),
     tf.keras.layers.Dense(1)]
)

# use mean squared error as the loss function
model.compile(optimizer=tf.keras.optimizers.SGD(0.01, 0.9), loss='mse')

r = model.fit(X, Y, epochs=3000)

# print time elapsed while training
print("training time: " + f'{(time.time() - start):.3f}' + "s")

# predict salaries for the next decade
X2020 = [[6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]
Y2020 = []

for Xfuture in X2020:
  a = model.predict(Xfuture)[0][0]
  Yfuture = np.power(np.e, a)
  Y2020.append(Yfuture)

for i in range(0,10):
  print(str(X2020[i][0]+2015) + ": " + str(np.trunc(Y2020.pop(0))))
