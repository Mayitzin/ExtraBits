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