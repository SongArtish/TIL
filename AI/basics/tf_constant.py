import tensorflow as tf

# Create a constant op
# This op is added as a NODE to the default graph
hello = tf.constant("Hello, TensorFlow!")

# run the op and get result
print(hello)