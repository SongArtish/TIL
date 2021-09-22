# Filtering Log: info = 1, warning = 2, error = 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np

# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

W= tf.Variable(tf.random.normal([1]), name='weight')
b= tf.Variable(tf.random.normal([1]), name='bias')

# Ourhypothesis XW+b
hypothesis = x_train * W + b

# cost/Loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# Minimize
'''
optimizer = tf.optimizers.GradientDescentOptimizer(learning_rate=0.001)
train = optimizer.minimize(cost) # minimize cost (adjusting tensor Variables)
'''

sgd = tf.keras.optimizers.SGD(learning_rate = 0.01)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim = 1))
model.compile(loss='mean_squared_error', optimizer=sgd)
model.fit(x_train,y_train, epochs=500)
print(model.predict(np.array([5]))) # predict 5 at the model
