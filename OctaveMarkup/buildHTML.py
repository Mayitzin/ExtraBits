# -*- coding: utf-8 -*-
"""
HTML file builder.

History:
    04.03.2016. First implementation.

@author: Mario Garcia
www.mayitzin.com
"""

def buildHTML(body,head):
    doctype = "<!DOCTYPE html>"
    html_open = "<html>"
    body = "<body>Hi!</body>"
    html_close = "</html>"
    return doctype+html_open+head+body+html_close

fileName = 'Output.html'

header = """
<head>
    <title>Test</title>
</head>
"""
body = "<body>Hi!</body>"

text = buildHTML(body,header)

with open(fileName, 'w') as outputFile:
    outputFile.write(text)