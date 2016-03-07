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


def getParticles(equation):
    n = len(equation)
    positions, particles = [], {}
    for i in range(n):
        if equation[i]=="(":
            positions.append(i)
        if equation[i]==")":
            part = equation[positions.pop():i+1]
            if part not in particles.keys(): particles[part] = 1
            else: particles[part] += 1
    return particles, positions


def replaceConst(equation):
    equation = equation.replace("dt**","dt")
    equation = equation.replace("dt^","dt")
    return equation


# Default File
fileName = None
# Get the Input File (if given)
if len(sys.argv) >= 2:
    if isFile(sys.argv[1]): fileName = sys.argv[1]
    else: print fileName, "is NOT a valid input File"

# Used Equation
equation = "(-(x6 - z0)*((P66*dt + Q36)*(P33*dt + P66*dt*hdt + Q03) - (P66*hdt + Q06)*(P33 + P66*dt**2 + Q33 + R99)) + ((P66*dt + Q36)*(P66*dt + Q63) - (P66 + Q66 + R00)*(P33 + P66*dt**2 + Q33 + R99))*(dt*x3 + hdt*x6 + x0) - ((P66*dt + Q63)*(P66*hdt + Q06) - (P66 + Q66 + R00)*(P33*dt + P66*dt*hdt + Q03))*(dt*x6 + x3 - z9))/((P66*dt + Q36)*(P66*dt + Q63) - (P66 + Q66 + R00)*(P33 + P66*dt**2 + Q33 + R99))"
# equation = "((((2*dt^2*x8+4*dt*x5+4*x2)*R1111+(2*dt^2*x8+4*dt*x5+4*x2)*Q55+(4*zvz-4*dt*x8-4*x5)*Q25+(2*dt^3*zvz+2*dt^3*x5+4*dt^2*x2)*P88+(4*dt*zvz-2*dt^2*x8+4*x2)*P55)*R1212+(4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*R1111+(4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*Q55+(-4*zpz*Q25-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q52+(-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q25+(4*dt^2*zpz*P88+4*zpz*P55)*Q22+(dt^4*zpz*P55+4*dt^2*zpz*P22)*P88+4*zpz*P22*P55)*R22+(((2*dt^2*x8+4*dt*x5+4*x2)*Q88+(4*zaz-4*x8)*Q28+(2*dt^2*zaz+4*dt*x5+4*x2)*P88)*R1111+((2*dt^2*x8+4*dt*x5+4*x2)*Q55+(4*zvz-4*dt*x8-4*x5)*Q25+(2*dt^3*zvz+2*dt^3*x5+4*dt^2*x2)*P88+(4*dt*zvz-2*dt^2*x8+4*x2)*P55)*Q88+((-2*dt^2*x8-4*dt*x5-4*x2)*Q58+(-4*zvz+4*dt*x8+4*x5)*Q28+(-2*dt^2*zvz-2*dt^2*x5-4*dt*x2)*P88)*Q85+((4*x8-4*zaz)*Q25+(-2*dt^3*zaz-4*dt^2*x5-4*dt*x2)*P88+(4*dt*x8-4*dt*zaz)*P55)*Q58+((4*zaz-4*x8)*Q28+(2*dt^2*zaz+4*dt*x5+4*x2)*P88)*Q55+((-4*dt*zvz+4*dt^2*zaz+4*dt*x5)*P88+(4*zaz-4*x8)*P55)*Q28+(4*zvz-4*dt*zaz-4*x5)*P88*Q25+(4*dt*zvz-2*dt^2*zaz+4*x2)*P55*P88)*R1212+((4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*Q88+(-4*zpz*Q28-2*dt^2*zpz*P88)*Q82-2*dt^2*zpz*P88*Q28+4*zpz*P88*Q22+(4*dt^2*zpz*P55+4*zpz*P22)*P88)*R1111+((4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*Q55+(-4*zpz*Q25-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q52+(-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q25+(4*dt^2*zpz*P88+4*zpz*P55)*Q22+(dt^4*zpz*P55+4*dt^2*zpz*P22)*P88+4*zpz*P22*P55)*Q88+((-4*zpz*Q22-dt^4*zpz*P88-4*dt^2*zpz*P55-4*zpz*P22)*Q58+(4*zpz*Q28+2*dt^2*zpz*P88)*Q52+(2*dt^3*zpz*P88+4*dt*zpz*P55)*Q28-4*dt*zpz*P88*Q22+(-2*dt^3*zpz*P55-4*dt*zpz*P22)*P88)*Q85+((4*zpz*Q25+2*dt^3*zpz*P88+4*dt*zpz*P55)*Q58+(-4*zpz*Q28-2*dt^2*zpz*P88)*Q55+(-4*dt^2*zpz*P88-4*zpz*P55)*Q28+4*dt*zpz*P88*Q25+2*dt^2*zpz*P55*P88)*Q82+(2*dt^2*zpz*P88*Q25-4*dt*zpz*P88*Q22+(-2*dt^3*zpz*P55-4*dt*zpz*P22)*P88)*Q58+(-2*dt^2*zpz*P88*Q28+4*zpz*P88*Q22+(4*dt^2*zpz*P55+4*zpz*P22)*P88)*Q55+(4*dt*zpz*P88*Q28-4*zpz*P88*Q25-4*dt*zpz*P55*P88)*Q52+2*dt^2*zpz*P55*P88*Q28-4*dt*zpz*P55*P88*Q25+4*zpz*P55*P88*Q22+4*zpz*P22*P55*P88)/(((4*R1111+4*Q55+4*dt^2*P88+4*P55)*R1212+(4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*R1111+(4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*Q55+(-4*Q25-2*dt^3*P88-4*dt*P55)*Q52+(-2*dt^3*P88-4*dt*P55)*Q25+(4*dt^2*P88+4*P55)*Q22+(dt^4*P55+4*dt^2*P22)*P88+4*P22*P55)*R22+((4*Q88+4*P88)*R1111+(4*Q55+4*dt^2*P88+4*P55)*Q88+(-4*Q58-4*dt*P88)*Q85-4*dt*P88*Q58+4*P88*Q55+4*P55*P88)*R1212+((4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*Q88+(-4*Q28-2*dt^2*P88)*Q82-2*dt^2*P88*Q28+4*P88*Q22+(4*dt^2*P55+4*P22)*P88)*R1111+((4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*Q55+(-4*Q25-2*dt^3*P88-4*dt*P55)*Q52+(-2*dt^3*P88-4*dt*P55)*Q25+(4*dt^2*P88+4*P55)*Q22+(dt^4*P55+4*dt^2*P22)*P88+4*P22*P55)*Q88+((-4*Q22-dt^4*P88-4*dt^2*P55-4*P22)*Q58+(4*Q28+2*dt^2*P88)*Q52+(2*dt^3*P88+4*dt*P55)*Q28-4*dt*P88*Q22+(-2*dt^3*P55-4*dt*P22)*P88)*Q85+((4*Q25+2*dt^3*P88+4*dt*P55)*Q58+(-4*Q28-2*dt^2*P88)*Q55+(-4*dt^2*P88-4*P55)*Q28+4*dt*P88*Q25+2*dt^2*P55*P88)*Q82+(2*dt^2*P88*Q25-4*dt*P88*Q22+(-2*dt^3*P55-4*dt*P22)*P88)*Q58+(-2*dt^2*P88*Q28+4*P88*Q22+(4*dt^2*P55+4*P22)*P88)*Q55+(4*dt*P88*Q28-4*P88*Q25-4*dt*P55*P88)*Q52+2*dt^2*P55*P88*Q28-4*dt*P55*P88*Q25+4*P55*P88*Q22+4*P22*P55*P88)"

equation = replaceConst(equation)
print equation
particles, positions = getParticles(equation)


repeated = []
for keys, values in particles.iteritems():
    if values>1: repeated.append(keys)

print "Repeated elements are:"
for elems in repeated: print str(particles[elems])+"x : ", elems