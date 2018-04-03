import tensorflow as tf
x_input = tf.placeholder(tf.float32)
y_output = tf.placeholder(tf.float32)
eps = 0.01
W1 = tf.Variable(tf.random_uniform([2,2], -eps, eps))
W2 = tf.Variable(tf.random_uniform([2,1], -eps, eps))
layer1 = tf.sigmoid(tf.matmul(x_input, W1))
output_layer = tf.sigmoid(tf.matmul(layer1, W2))
cost = tf.reduce_mean(tf.square(y_output - output_layer))
train = tf.train.GradientDescentOptimizer(0.05).minimize(cost)
training_data = ([[0,0],[0,1],[1,0],[1,1]], [[0],[1],[1],[0]])
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(5000):
        sess.run(train, feed_dict={x_input: training_data[0], y_output: training_data[1]}) 
