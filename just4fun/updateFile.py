# -*- coding: utf-8 -*-
"""
Update Files

@author: Mario Garcia
www.mayitzin.com
"""

import sys
from collections import OrderedDict

fileName = "defaultFile.txt"

if len(sys.argv) >= 2:
    fileName = sys.argv[1]
    print "Your given data file is %s"%fileName

if "-c" in sys.argv:
    calFile = sys.argv[sys.argv.index("-c")+1]
    print "You gave %s as calibration File"%calFile

parameters = OrderedDict([
    # Scaling and Bias of Magnetometer
    ('scm' , 1.0),  ('bmx' , 0.0),  ('bmy' , 0.0),  ('bmz' , 0.0),
    # Gravity Force
    ('gf' , 9.813),
    # Process Noise Variances
    ('q_p' , 0.1), ('q_v' , 0.1), ('q_a' , 0.1), ('q_g' , 0.1), ('q_m' , 0.1),
    # Sensor Noise Variances
    ('r_a' , 0.1), ('r_g' , 0.1), ('r_m' , 0.1), ('r_v' , 0.1), ('r_p' , 0.1) ])

params = parameters.keys()

paramsToUpdate = {"bmy":1.1}

fo = open(calFile, "r+")
print "name of File: %s"%fo.name
print "Parameter to Update:"
for line in fo:
    if not line.startswith("//"):
        pair = line.strip('\n').split(":")
        if pair[0] in paramsToUpdate.keys(): print pair[0], "with", paramsToUpdate[pair[0]]

fo.close()


import fileinput
for line in fileinput.input(calFile, inplace=True):
    if not line.startswith("//"):
        pair = line.strip('\n').split(":")
        if pair[0] in paramsToUpdate.keys():
            print pair[0]+":"+str(paramsToUpdate[pair[0]])
        else:
            print line.strip('\n')
    else:
        print line.strip('\n')




with open(calFile, 'a+') as f:
    read_data = f.readlines()

new_param, new_value = "bmy", 1.1

# Remove lines starting with "//"
[read_data.remove(line) for line in read_data if line.startswith("//")]
# Find parameters in File
foundParams = []
for param in read_data:
    pair = param.strip('\n').split(":")
    if pair[0] in params: foundParams.append(pair[0])

if len(foundParams)>0:
    print "Found Parameters:"
    for param in foundParams: print "   "+param
