# -*- coding: utf-8 -*-
"""
Simplify Equations

@author: Mario Garcia
www.mayitzin.com
"""

import sys
import re


def isFile(inputFile):
    validFiles = [".csv", ".txt"]
    if inputFile[-4:] in validFiles: return True
    else: return False


def getParticles(dummy):
    n = len(dummy)
    positions, particles = [], {}
    for i in range(n):
        if dummy[i]=="(":
            positions.append(i)
        if dummy[i]==")":
            part = dummy[positions.pop():i+1]
            if part not in particles.keys(): particles[part] = 1
            else: particles[part] += 1
    return particles, positions


def replaceConst(dummy):
    dummy = dummy.replace("dt**","dt")
    dummy = dummy.replace("dt^","dt")
    return dummy


