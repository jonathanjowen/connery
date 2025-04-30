#!/bin/python3

import numpy

def read_float():
    """Return a float read from STDIN."""
    return(float(input()))

def read_floats(sep=None):
    """Return an iterator of floats from a STDIN line."""  
    return(map(float, input().split(sep)))
    
if __name__ == '__main__':
    coefficients = numpy.array(list(read_floats())[::-1])
    x = read_float()
    
    p = numpy.polynomial.Polynomial(coefficients)
    print(p(x))

    

# https://www.hackerrank.com/challenges/np-polynomials/problem