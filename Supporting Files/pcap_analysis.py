import tensorflow as tf
import pandas

hello = tf.constant('hi')
sess = tf.Session()
print(sess.run(hello))

newestSet = pandas.read_csv('new.csv')
y, X = pandas.train(['Classification']), pandas.train([['DGMLEN', 'IPLEN', 'IP']], dtype='object')
