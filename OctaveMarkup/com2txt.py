"""
Parser of M-files to get the info from comments.

History:
    24.05.2015. First implementation.

@author: Mario Garcia
www.mayitzin.com
"""

f = open('dlt.m', 'r')
t = open('test.txt', 'w')
for line in f:
    l = line[0:-1]
    try:
        t.write( l[l.index('%')+1:]+"\n" )
    except:
        pass

t.close()
f.close()