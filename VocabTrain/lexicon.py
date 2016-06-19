"""
This script creates, modifies and removes a quasi-database of a lexicon using
JSON formatted data.
"""

import json

dic_EN_GE = {"label1":"label"}

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], sort_keys=True, indent=4)