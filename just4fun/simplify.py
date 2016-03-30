# -*- coding: utf-8 -*-
"""
Simplify Equations

@author: Mario Garcia
www.mayitzin.com
"""

import sys
import re


def isFile(inputFile):
    """This function determines wether the given file is a valid file or not.
    The valid files bz now are CSV and plain Text files.
    """
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


def getTerms(particles, debug=False):
    repeated, unique = [], []
    for keys, values in particles.iteritems():
        if values>1: repeated.append(keys)
    for i in range(len(repeated)):
        elem = repeated[i]
        for j in repeated:
            if elem in j and(elem is not j): unique.append(elem)
    if len(unique)>0:
        if debug:
            print "Unique elements are:"
            for elems in unique: print elems
        else: pass
    else:
        unique = repeated
    return unique, repeated


def getVariables(elements):
    atoms = re.split(r'[ +-]', element[1:-1])
    atoms = [x for x in atoms if x]
    return atoms


def buildVars(terms):
    var_list = []
    for i in range(len(terms)):
        eltm = filter(None, re.split(r'[ +*-]',terms[i][1:-1]))
        newterm = u""
        for ch in eltm:
            newterm+=ch[0]
            if ch == eltm[-1]: newterm+=ch[1:]
        if newterm[0].isnumeric(): newterm = "_"+newterm
        var_list.append(newterm)
    return var_list


def countOps(equation):
    num_pw1, num_pw2 = equation.count("**"), equation.count("^")
    num_mul, num_div = equation.count("*"), equation.count("/")
    num_sum, num_sub = equation.count("+"), equation.count("-")
    return num_pw1+num_pw2+num_mul+num_div+num_sum+num_sub


def simplify(equation, debug=False):
    # Remove repeated constants
    equation = replaceConst(equation)
    # Get each individual term of the equation
    particles, positions = getParticles(equation)
    # Get unique terms
    terms, repeated = getTerms(particles)
    # Build Variable names for each unique term
    varl = buildVars(repeated)
    # Substitute elements in new equation
    new_equation = equation
    for i in range(len(varl)):
        # Jump step if is a contained set of expressions
        if varl[i].startswith('('): continue
        # Print the substitutions out if in Debug mode
        if debug: print "  "+str(equation.count(repeated[i]))+"x ",varl[i],"  :\t",repeated[i]
        # Substitute selected term with its corresponding abbreviation
        new_equation = new_equation.replace( repeated[i] , varl[i] )
    return new_equation


# Default Equation
# default_eq = "(-(x6 - z0)*((P66*dt + Q36)*(P33*dt + P66*dt*hdt + Q03) - (P66*hdt + Q06)*(P33 + P66*dt**2 + Q33 + R99)) + ((P66*dt + Q36)*(P66*dt + Q63) - (P66 + Q66 + R00)*(P33 + P66*dt**2 + Q33 + R99))*(dt*x3 + hdt*x6 + x0) - ((P66*dt + Q63)*(P66*hdt + Q06) - (P66 + Q66 + R00)*(P33*dt + P66*dt*hdt + Q03))*(dt*x6 + x3 - z9))/((P66*dt + Q36)*(P66*dt + Q63) - (P66 + Q66 + R00)*(P33 + P66*dt**2 + Q33 + R99))"
default_eq = "((((2*dt^2*x8+4*dt*x5+4*x2)*R1111+(2*dt^2*x8+4*dt*x5+4*x2)*Q55+(4*zvz-4*dt*x8-4*x5)*Q25+(2*dt^3*zvz+2*dt^3*x5+4*dt^2*x2)*P88+(4*dt*zvz-2*dt^2*x8+4*x2)*P55)*R1212+(4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*R1111+(4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*Q55+(-4*zpz*Q25-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q52+(-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q25+(4*dt^2*zpz*P88+4*zpz*P55)*Q22+(dt^4*zpz*P55+4*dt^2*zpz*P22)*P88+4*zpz*P22*P55)*R22+(((2*dt^2*x8+4*dt*x5+4*x2)*Q88+(4*zaz-4*x8)*Q28+(2*dt^2*zaz+4*dt*x5+4*x2)*P88)*R1111+((2*dt^2*x8+4*dt*x5+4*x2)*Q55+(4*zvz-4*dt*x8-4*x5)*Q25+(2*dt^3*zvz+2*dt^3*x5+4*dt^2*x2)*P88+(4*dt*zvz-2*dt^2*x8+4*x2)*P55)*Q88+((-2*dt^2*x8-4*dt*x5-4*x2)*Q58+(-4*zvz+4*dt*x8+4*x5)*Q28+(-2*dt^2*zvz-2*dt^2*x5-4*dt*x2)*P88)*Q85+((4*x8-4*zaz)*Q25+(-2*dt^3*zaz-4*dt^2*x5-4*dt*x2)*P88+(4*dt*x8-4*dt*zaz)*P55)*Q58+((4*zaz-4*x8)*Q28+(2*dt^2*zaz+4*dt*x5+4*x2)*P88)*Q55+((-4*dt*zvz+4*dt^2*zaz+4*dt*x5)*P88+(4*zaz-4*x8)*P55)*Q28+(4*zvz-4*dt*zaz-4*x5)*P88*Q25+(4*dt*zvz-2*dt^2*zaz+4*x2)*P55*P88)*R1212+((4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*Q88+(-4*zpz*Q28-2*dt^2*zpz*P88)*Q82-2*dt^2*zpz*P88*Q28+4*zpz*P88*Q22+(4*dt^2*zpz*P55+4*zpz*P22)*P88)*R1111+((4*zpz*Q22+dt^4*zpz*P88+4*dt^2*zpz*P55+4*zpz*P22)*Q55+(-4*zpz*Q25-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q52+(-2*dt^3*zpz*P88-4*dt*zpz*P55)*Q25+(4*dt^2*zpz*P88+4*zpz*P55)*Q22+(dt^4*zpz*P55+4*dt^2*zpz*P22)*P88+4*zpz*P22*P55)*Q88+((-4*zpz*Q22-dt^4*zpz*P88-4*dt^2*zpz*P55-4*zpz*P22)*Q58+(4*zpz*Q28+2*dt^2*zpz*P88)*Q52+(2*dt^3*zpz*P88+4*dt*zpz*P55)*Q28-4*dt*zpz*P88*Q22+(-2*dt^3*zpz*P55-4*dt*zpz*P22)*P88)*Q85+((4*zpz*Q25+2*dt^3*zpz*P88+4*dt*zpz*P55)*Q58+(-4*zpz*Q28-2*dt^2*zpz*P88)*Q55+(-4*dt^2*zpz*P88-4*zpz*P55)*Q28+4*dt*zpz*P88*Q25+2*dt^2*zpz*P55*P88)*Q82+(2*dt^2*zpz*P88*Q25-4*dt*zpz*P88*Q22+(-2*dt^3*zpz*P55-4*dt*zpz*P22)*P88)*Q58+(-2*dt^2*zpz*P88*Q28+4*zpz*P88*Q22+(4*dt^2*zpz*P55+4*zpz*P22)*P88)*Q55+(4*dt*zpz*P88*Q28-4*zpz*P88*Q25-4*dt*zpz*P55*P88)*Q52+2*dt^2*zpz*P55*P88*Q28-4*dt*zpz*P55*P88*Q25+4*zpz*P55*P88*Q22+4*zpz*P22*P55*P88)/(((4*R1111+4*Q55+4*dt^2*P88+4*P55)*R1212+(4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*R1111+(4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*Q55+(-4*Q25-2*dt^3*P88-4*dt*P55)*Q52+(-2*dt^3*P88-4*dt*P55)*Q25+(4*dt^2*P88+4*P55)*Q22+(dt^4*P55+4*dt^2*P22)*P88+4*P22*P55)*R22+((4*Q88+4*P88)*R1111+(4*Q55+4*dt^2*P88+4*P55)*Q88+(-4*Q58-4*dt*P88)*Q85-4*dt*P88*Q58+4*P88*Q55+4*P55*P88)*R1212+((4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*Q88+(-4*Q28-2*dt^2*P88)*Q82-2*dt^2*P88*Q28+4*P88*Q22+(4*dt^2*P55+4*P22)*P88)*R1111+((4*Q22+dt^4*P88+4*dt^2*P55+4*P22)*Q55+(-4*Q25-2*dt^3*P88-4*dt*P55)*Q52+(-2*dt^3*P88-4*dt*P55)*Q25+(4*dt^2*P88+4*P55)*Q22+(dt^4*P55+4*dt^2*P22)*P88+4*P22*P55)*Q88+((-4*Q22-dt^4*P88-4*dt^2*P55-4*P22)*Q58+(4*Q28+2*dt^2*P88)*Q52+(2*dt^3*P88+4*dt*P55)*Q28-4*dt*P88*Q22+(-2*dt^3*P55-4*dt*P22)*P88)*Q85+((4*Q25+2*dt^3*P88+4*dt*P55)*Q58+(-4*Q28-2*dt^2*P88)*Q55+(-4*dt^2*P88-4*P55)*Q28+4*dt*P88*Q25+2*dt^2*P55*P88)*Q82+(2*dt^2*P88*Q25-4*dt*P88*Q22+(-2*dt^3*P55-4*dt*P22)*P88)*Q58+(-2*dt^2*P88*Q28+4*P88*Q22+(4*dt^2*P55+4*P22)*P88)*Q55+(4*dt*P88*Q28-4*P88*Q25-4*dt*P55*P88)*Q52+2*dt^2*P55*P88*Q28-4*dt*P55*P88*Q25+4*P55*P88*Q22+4*P22*P55*P88)"

# Default File
fileName = None
# Get the Input File (if given)
if len(sys.argv) >= 2:
    if isFile(sys.argv[1]): fileName = sys.argv[1]
    else: print fileName, "is NOT a valid input File"

if fileName is not None:
    with open(fileName, 'r') as f:
        read_eqs = f.read().splitlines()    # Read lines without return carriage
    read_eqs = filter(None, read_eqs)       # Remove empty lines
    num_eqs = len(read_eqs)                 # Number of read lines
    print "  Read equations:", num_eqs
    for i in range(num_eqs):
        equation = read_eqs[i]
        print "\n  --------------- RESULTS OF EQUATION %d ---------------"%(i+1)
        # Used Equation
        print equation
        num_pw1, num_pw2 = equation.count("**"), equation.count("^")
        num_mul, num_div = equation.count("*"), equation.count("/")
        num_sum, num_sub = equation.count("+"), equation.count("-")
        print "Total of", num_pw1+num_pw2+num_mul+num_div+num_sum+num_sub, "operations BEFORE simplification\n"

        # First simplification
        new_equation   = simplify(equation, True)
        # Second simplification
        new_equation_2 = simplify(new_equation, True)

        print new_equation_2
        num_pw1, num_pw2 = new_equation_2.count("**"), new_equation_2.count("^")
        num_mul, num_div = new_equation_2.count("*"), new_equation_2.count("/")
        num_sum, num_sub = new_equation_2.count("+"), new_equation_2.count("-")
        print "Total of", num_pw1+num_pw2+num_mul+num_div+num_sum+num_sub, "operations AFTER simplification"
else:
    equation = default_eq
    print "Using default equation"
