"""
Testing file for Neural Networks

Following tutorial and code from:
http://www.existor.com/en/ml-neural-networks.html

@author: Mario Garcia
"""

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1./(1+np.exp(-x))

def nn_tanh(x):
    return np.tanh(x)

x = 0.0
print "sigmoid(%.5f) = %.5f" % (x,sigmoid(x))
print "tanh(%.5f) = %.5f" % (x,nn_tanh(x))

t = np.arange(-5.0, 5.0, 0.01)

l1 = plt.plot(t, sigmoid(t), 'r-')
l2 = plt.plot(t, nn_tanh(t), 'g-')

plt.show()
