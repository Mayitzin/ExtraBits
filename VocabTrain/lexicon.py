"""
This script creates, modifies and removes a quasi-database of a lexicon using
JSON formatted data.

TODO: Make a good interpretation of stored data. Maybe parse as dictionary.
"""

import json
from datetime import datetime

def saveData(data, fileName="output.txt"):
    # Save to a file
    with open(fileName, 'a') as outfile:
        outfile.write(data)

def readData(fileName, printOut=False):
    with open(fileName, 'r') as inFile:
        read_lines = inFile.readlines()
    if len(read_lines)>0 and printOut:
        for line in read_lines:
            print line.strip()
            #print line.strip()[1:-1]
            #print line.strip().split(',')

dic_EN_GE = {"label1":"label"}

t = datetime.now().isoformat()

#s = [t, {'bar': ('baz', None, 1.0, 2)}]
d = {t: {'bar': ('baz', None, 1.0, 2)}}


# Compact encoding
#data_line = json.dumps(s, sort_keys=True, separators=(',',':')) + "\n"
data_line = json.dumps(d, sort_keys=True, separators=(',',':')) + "\n"

# Save to a file
saveData(data_line, "output.txt")
readData("output.txt", printOut=True)