# Filtering Log: info = 1, warning = 2, error = 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)    # also tf.float32 implicitly

@tf.function
def add():
    return node1 + node2

print("node1:", node1, "node2:", node2)
print("node3:", add())