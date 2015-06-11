"""
This script will show a text in Braile code on screen, built from a given
normal text.

History:
	11.06.2015. First implementation.

@author: Mario Garcia
www.mayitzin.com
"""

import numpy as np


def build_code(c):
	# Basic particles of Braile Code
	x1 = np.array([0,0])
	x2 = np.array([0,1])
	x3 = np.array([1,0])
	x4 = np.array([1,1])
	n1 = np.array([[1,0],[0,0]])
	n2 = np.array([[1,0],[1,0]])
	n3 = np.array([[1,1],[0,0]])
	n4 = np.array([[1,1],[0,1]])
	n5 = np.array([[1,0],[0,1]])
	n6 = np.array([[1,1],[1,0]])
	n7 = np.array([[1,1],[1,1]])
	n8 = np.array([[1,0],[1,1]])
	n9 = np.array([[0,1],[1,0]])
	n0 = np.array([[0,1],[1,1]])
	# Table of Braile Code made of particles from above
	codes = {
	'a' : np.vstack((n1,x1)),
	'b' : np.vstack((n2,x1)),
	'c' : np.vstack((n3,x1)),
	'd' : np.vstack((n4,x1)),
	'e' : np.vstack((n5,x1)),
	'f' : np.vstack((n6,x1)),
	'g' : np.vstack((n7,x1)),
	'h' : np.vstack((n8,x1)),
	'i' : np.vstack((n9,x1)),
	'j' : np.vstack((n0,x1))
	}
	return codes[c]


text = "abeja"
txt_ls = list(text)
txt_bl = build_code(txt_ls[0])

for c in txt_ls[1:]:
	txt_bl = np.hstack((txt_bl,build_code(c)))

print txt_ls, ":"
print txt_bl

print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      for row in txt_bl]))