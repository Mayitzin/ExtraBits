"""Tupper's self-referential formula.

This is a simple implementation of Tupper's self-referential formula, a.k.a. the
everything-plot formula, as Matt Parker named it.

@author: Mario Garcia
"""
import matplotlib.image as mpimg
import numpy as np

def img2txt(image):
    pixelated_image = []
    for line in image:
        int_line = [int(x) for x in line]
        joined_line = ''.join(map(str, int_line))
        pixelated_line = ''.join(' ' if x=='0' else 'M' for x in joined_line)
        pixelated_image.append(pixelated_line)
    return pixelated_image

def compute_k(image):
    string_list = []
    rotated_image = np.rot90(image, 3)
    for line in rotated_image:
        int_line = [int(x) for x in line]
        joined_line = ''.join(map(str, int_line))
        inverted_line = ''.join('1' if x=='0' else '0' for x in joined_line)
        string_list.append(inverted_line)
    joined_string = ''.join(string_list)
    k = int(joined_string, 2)
    return k

if __name__ == "__main__":
    import sys

    img_file = 'test1.png'
    if len(sys.argv)>1:
        img_file = sys.argv[1]

    image = mpimg.imread(img_file)[:,:,0]
    print "Using file", img_file

    k = compute_k(image)
    print k

    pixelated_image = img2txt(image)
