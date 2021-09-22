## NO LONGER AVAILABLE IN VERSION 2.00 OR MORE

import tensorflow as tf

sess = tf.Session()

# 1. Build graph using TensorFlow operations
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a,b)

# 2. feed data and run graph (operation)
print(sess.run(adder_node, feed_dict = {a : 3, b : 4.5}))
print(sess.run(adder_node, feed_dict = {a : [1, 3], b : [2, 4]}))

# 3. update variables in the graph and return values