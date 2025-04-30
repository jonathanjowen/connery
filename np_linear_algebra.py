#!/bin/python3

import numpy

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))

def read_floats(sep=None):
    """Return an iterator of floats from a STDIN line."""  
    return(map(float, input().split(sep)))
    
if __name__ == '__main__':
    n = read_integer()
    list_a = []
    for _ in range(n):
        list_a += [list(read_floats())]
    a = numpy.array(list_a)
    det_a = numpy.linalg.det(a)
    print(numpy.round(det_a, 2))

    

# https://www.hackerrank.com/challenges/np-linear-algebra/problem