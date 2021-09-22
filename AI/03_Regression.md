# Regression

2021.08.20

---

[TOC]

---



## Linear Regression

### 1. Form

$$
H(x) = Wx+b
$$

```python
# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

W= tf.Variable(tf.random.normal([1]), name='weight')
b= tf.Variable(tf.random.normal([1]), name='bias')

# Ourhypothesis XW+b
hypothesis = x_train * W + b

'''
# `tf.Variable` refers to trainable variable
# `[1]` represents shape (1st dimension)
'''
```



### 2. Cost/Loss Function

> how fit the line to our (training) data?

- m: number of data
- :pushpin:**​ minimize cost(W, b)**

$$
cost(W,b) = \frac{1}{m}\sum_{i=1}^m (H(x^i)-y^i)^2
$$

```python
# cost/Loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))
'''
# `tf.reduce_mean(t)` returns mean value
'''
```



### 3. Minimize

```python
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
```

- SGD: Stochastic Gradient Descent
