"""
Parser of M-files to get the info from comments.

History:
    24.05.2015. First implementation.
    01.02.2016. Using NLTK

@author: Mario Garcia
www.mayitzin.com
"""

import nltk

fileName = 'rotation.m'

with open(fileName, 'r') as inputFile:
    text = inputFile.readlines()

m = len(text)
lines = []

for i in range(m):
	if text[i][0] == "%":
		lines.append(text[i])
		ttype = "block"
		print i, nltk.word_tokenize(text[i])
		# print i, ":", len(text[i]), ":", text[i][:-1]

print nltk.word_tokenize(lines[0])
print fileName[:-2].upper()

if nltk.word_tokenize(lines[1])==fileName[:-2].upper():
	print "the title of the function is", fileName[:-2]
else:
	print "The name of the file does not correspond to the title"