import tensorflow as tf
import numpy as np
import time
import datetime
start_time = time.time()
end_time = time.time()

matrix1 = tf.constant([[3., 3.]])

matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)
sess = tf.Session()
result = sess.run(product)
print (result)
sess.close()

