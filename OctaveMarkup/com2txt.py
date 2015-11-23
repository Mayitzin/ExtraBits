"""
Parser of M-files to get the info from comments.

History:
    24.05.2015. First implementation.

@author: Mario Garcia
www.mayitzin.com
"""

with open('rotation.m', 'r') as inputFile:
    text = inputFile.readlines()

m = len(text)

for i in range(m):
	if text[i][0] == "%":
		ttype = "block"
		print text[i]

print "Finished"