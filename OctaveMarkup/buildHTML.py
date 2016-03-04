# -*- coding: utf-8 -*-
"""
HTML file builder.

History:
    04.03.2016. First implementation.

@author: Mario Garcia
www.mayitzin.com
"""

fileName = 'Output.html'

text = """<!DOCTYPE html>
<html>
<head>
<title>Test</title>
</head>
<body>
Hi!
</body>
</html>"""

with open(fileName, 'w') as outputFile:
    outputFile.write(text)
