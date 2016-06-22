"""
Testing file for Neural Networks

Following tutorial and code from:
http://www.existor.com/en/ml-neural-networks.html

@author: Mario Garcia
"""

import numpy as np
import matplotlib.pyplot as plt

def w_sums(x, w):
    if len(np.shape(w))<2:
        z = np.array([[0.0]])
        w = np.array(w).reshape((len(w),1))
    else:
        z = np.zeros((np.shape(w)[0],1))
    print np.shape(z)
    print np.shape(w)
    for i in range(np.shape(w)[0]):
        for j in range(np.shape(z)[1]):
            print "w[%d,%d]=%f"%(i,j,w[i,j])
            # z[i] += x[i]*w[i,j]
    return z

def sigmoid(x):
    return 1./(1+np.exp(-x))

def nn_tanh(x):
    return np.tanh(x)

def logloss(y, p):
    J = 0.0
    for j in range(len(y)):
        J += y[j]*np.log(p[j])
    return -J

x = 0.2
print "sigmoid(%.4f) = %.4f" % (x,sigmoid(x))
print "tanh(%.4f) = %.4f" % (x,nn_tanh(x))


x = np.array([1, 0, 0])
w = np.array([0.2, -0.03, 0.14])
z = w_sums(x, w)
print "Returned:\n", z

# W = np.array([[0.2, 0.15, -0.01],
#               [0.01, -0.1, -0.06],
#               [0.14, -0.2, -0.03]])
# print W
# print w_sums(x, W)

# t = np.arange(-5.0, 5.0, 0.01)
# l1 = plt.plot(t, sigmoid(t), 'r-')
# l2 = plt.plot(t, nn_tanh(t), 'g-')
# plt.show()
