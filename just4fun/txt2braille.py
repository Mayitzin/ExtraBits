"""
This script will show a text in Braille code on screen, built from a given
normal text.

History:
    11.06.2015. First implementation.
    12.06.2015. Complete alphabet added.
    22.06.2015. Uppercase letters added.

@author: Mario Garcia
www.mayitzin.com
"""

import numpy as np


def build_code(c):
    # Basic particles of Braille Code
    x1 = np.array(['.','.'])
    x2 = np.array(['.','O'])
    x3 = np.array(['O','.'])
    x4 = np.array(['O','O'])
    n1 = np.array([['O','.'],['.','.']])
    n2 = np.array([['O','.'],['O','.']])
    n3 = np.array([['O','O'],['.','.']])
    n4 = np.array([['O','O'],['.','O']])
    n5 = np.array([['O','.'],['.','O']])
    n6 = np.array([['O','O'],['O','.']])
    n7 = np.array([['O','O'],['O','O']])
    n8 = np.array([['O','.'],['O','O']])
    n9 = np.array([['.','O'],['O','.']])
    n0 = np.array([['.','O'],['O','O']])
    ns = np.array([[' ',' '],[' ',' '],[' ',' ']])
    cp = np.array([['.','.'],['.','.'],['.','O']])
    # Table of Braille Code made of particles from above
    codes = {
    'a' : np.vstack((n1,x1)),
    'b' : np.vstack((n2,x1)),
    'c' : np.vstack((n3,x1)),
    'd' : np.vstack((n4,x1)),
    'e' : np.vstack((n5,x1)),
    'f' : np.vstack((n6,x1)),
    'g' : np.vstack((n7,x1)),
    'h' : np.vstack((n8,x1)),
    'i' : np.vstack((n9,x1)),
    'j' : np.vstack((n0,x1)),
    'k' : np.vstack((n1,x3)),
    'l' : np.vstack((n2,x3)),
    'm' : np.vstack((n3,x3)),
    'n' : np.vstack((n4,x3)),
    'o' : np.vstack((n5,x3)),
    'p' : np.vstack((n6,x3)),
    'q' : np.vstack((n7,x3)),
    'r' : np.vstack((n8,x3)),
    's' : np.vstack((n9,x3)),
    't' : np.vstack((n0,x3)),
    'u' : np.vstack((n1,x4)),
    'v' : np.vstack((n2,x4)),
    'x' : np.vstack((n3,x4)),
    'y' : np.vstack((n4,x4)),
    'z' : np.vstack((n5,x4)),
    ' ' : ns
    }
    if c.islower() or c.isspace():
        return codes[c]
    elif c.isupper():
        return np.hstack((cp,codes[c.lower()]))


def get_bl(txt_ls):
    txt_bl = build_code(txt_ls[0])
    for c in txt_ls[1:]:
        txt_bl = np.hstack((txt_bl,build_code(c)))
    return txt_bl


def print_code(text, txt_bl):
    for row in txt_bl:
        line = []
        for item in row: line.append(item)
        print ' '.join(line)
    # print ' '+'   '.join(list(text))


if __name__ == "__main__":
    import sys

    text = "mayitzin did this"
    if len(sys.argv) > 1:
        text = str(sys.argv[1])

    txt_bl = get_bl(list(text))
    print_code(text, txt_bl)