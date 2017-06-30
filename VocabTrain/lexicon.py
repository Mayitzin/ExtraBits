"""
This script creates, modifies and removes a quasi-database of a lexicon using
JSON formatted data.

TODO: Make a good interpretation of stored data. Maybe parse as dictionary.
"""

import json
from datetime import datetime


class Word:
    kind = 'word'

    def __init__(self, word):
        self.word = word
        self.translations = {}

    def add_translation(self, translation):
        self.translations.update(translation)

    def available_translations(self):
        return list(self.translations.keys())

    def toDict(self):
        d = {"word" : self.word}
        d.update({"translations" : self.translations})
        return d



def saveData(data, fileName="output.txt"):
    # Save to a file
    with open(fileName, 'a') as outfile:
        outfile.write(data)

def readData(fileName, printOut=False):
    with open(fileName, 'r') as inFile:
        read_lines = inFile.readlines()
    print("Read", len(read_lines), "lines")
    if len(read_lines)>0 and printOut:
        for line in read_lines:
            print(line.strip())
        last_line = read_lines[-1]
        new_d = json.loads(last_line)
        print(json.dumps(new_d, sort_keys=True, indent=4))

def newEntry():
    t = datetime.now().isoformat()
    d = {t: {'bar': ('baz', None, 1.0, 2)}}
    return d



haus = Word("Haus")
haus.add_translation({"es_mx":"casa"})
haus.add_translation({"en_us":"house"})
print("Available translations:", haus.available_translations())
d = haus.toDict()
print(d)
d_01 = {"es_mx":"chante"}
haus.add_translation(d_01)
print(d)


# d = newEntry()
# # Compact encoding
# data_line = json.dumps(d, sort_keys=True, separators=(',',':')) + "\n"
# # Save to a file
# saveData(data_line, "output.txt")
# readData("output.txt", printOut=True)