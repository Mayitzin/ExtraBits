"""
Testing file for Neural Networks

Following tutorial and code from:
http://www.existor.com/en/ml-neural-networks.html

@author: Mario Garcia
"""

import numpy as np
# import matplotlib.pyplot as plt

def w_sums(x, w):
    return np.dot(x,w)

def sigmoid(x):
    return 1./(1+np.exp(-x))

def nn_tanh(x):
    return np.tanh(x)

def softmax(z):
    return np.exp(z)/np.sum(np.exp(z))

def logloss(p, y):
    return -np.dot(y,np.log(p))


x = 0.2
print "sigmoid(%.4f) = %.4f" % (x,sigmoid(x))
print "tanh(%.4f) = %.4f" % (x,nn_tanh(x))


x = np.array([1, 0, 0])
w = np.array([0.2, -0.03, 0.14])
z = w_sums(x, w)

W = np.array([[[0.2, 0.15, -0.01],
               [0.01, -0.1, -0.06],
               [0.14, -0.2, -0.03]],
              [[0.08, 0.11, -0.3],
               [0.1, -0.15, 0.08],
               [0.1, 0.1, -0.07]]])
z1 = w_sums(x, W[0,:,:])
h1 = nn_tanh(z1)
print h1

z2 = w_sums(h1, W[1,:,:])
h2 = nn_tanh(z2)
p = softmax(h2)
print h2
print p

y = np.array([0, 1, 0])
print logloss(p,y)

# t = np.arange(-5.0, 5.0, 0.01)
# l1 = plt.plot(t, sigmoid(t), 'r-')
# l2 = plt.plot(t, nn_tanh(t), 'g-')
# plt.show()
